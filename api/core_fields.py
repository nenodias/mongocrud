from django.core.exceptions import ValidationError
from django.utils.encoding import smart_str

from rest_framework import serializers

from bson.errors import InvalidId
from mongoengine import dereference
from mongoengine.base.document import BaseDocument
from mongoengine.document import Document
from mongoengine.fields import ObjectId

from bson import Binary
from mongoengine.python_support import (PY3, bin_type, txt_type, str_types, StringIO)


class DocumentField(serializers.Field):
    """
    Base field for Mongoengine fields that we can not convert to DRF fields.

    To Contributors:
        - You can subclass DocumentField to implement custom (de)serialization
    """

    type_label = 'DocumentField'

    def __init__(self, *args, **kwargs):
        try:
            self.model_field = kwargs.pop('model_field')
            self.depth = kwargs.pop('depth')
        except KeyError:
            raise ValueError("%s requires 'model_field' kwarg" % self.type_label)

        super(DocumentField, self).__init__(*args, **kwargs)

    def transform_document(self, document, depth):
        data = {}

        # serialize each required field
        for field in document._fields:
            if hasattr(document, smart_str(field)):
                # finally check for an attribute 'field' on the instance
                obj = getattr(document, field)
            else:
                continue

            val = self.transform_object(obj, depth-1)

            if val is not None:
                data[field] = val

        return data

    def transform_dict(self, obj, depth):
        return dict([(key, self.transform_object(val, depth-1))
                     for key, val in obj.items()])

    def transform_object(self, obj, depth):
        """
        Models to natives
        Recursion for (embedded) objects
        """
        if isinstance(obj, BaseDocument):
            # Document, EmbeddedDocument
            if depth == 0:
                # Return primary key if exists, else return default text
                return smart_str(getattr(obj, 'pk', 'Max recursion depth exceeded'))
            return self.transform_document(obj, depth)
        elif isinstance(obj, dict):
            # Dictionaries
            return self.transform_dict(obj, depth)
        elif isinstance(obj, list):
            # List
            return [self.transform_object(value, depth) for value in obj]
        elif obj is None:
            return None
        else:
            return smart_str(obj) if isinstance(obj, ObjectId) else obj

    def to_internal_value(self, data):
        return self.model_field.to_python(data)

    def to_representation(self, value):
        return self.transform_object(value, self.depth - 1)


class ReferenceField(DocumentField):
    """
    For ReferenceField.
    We always dereference DBRef object before serialization
    TODO: Maybe support DBRef too?
    """

    type_label = 'ReferenceField'

    def to_internal_value(self, data):
        try:
            dbref = self.model_field.to_python(data)
        except InvalidId:
            raise ValidationError(self.error_messages['invalid'])

        instance = dereference.DeReference()([dbref])[0]

        # Check if dereference was successful
        if not isinstance(instance, Document):
            msg = self.error_messages['invalid']
            raise ValidationError(msg)

        return instance

    def to_representation(self, value):
        return self.transform_object(value, self.depth - 1)


class ListField(DocumentField):

    type_label = 'ListField'

    def to_internal_value(self, data):
        return self.model_field.to_python(data)

    def to_representation(self, value):
        return self.transform_object(value, self.depth - 1)


class EmbeddedDocumentField(DocumentField):

    type_label = 'EmbeddedDocumentField'

    def __init__(self, *args, **kwargs):
        try:
            self.document_type = kwargs.pop('document_type')
        except KeyError:
            raise ValueError("EmbeddedDocumentField requires 'document_type' kwarg")

        super(EmbeddedDocumentField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        if value is None:
            return None
        else:
            return self.transform_object(value, self.depth)

    def to_internal_value(self, data):
        return self.model_field.to_python(data)


class DynamicField(DocumentField):

    type_label = 'DynamicField'

    def __init__(self, field_name=None, source=None, *args, **kwargs):
        super(DynamicField, self).__init__(*args, **kwargs)
        self.field_name = field_name
        self.source = source
        if source:
            self.source_attrs = self.source.split('.')

    def to_representation(self, value):
        return self.model_field.to_python(value)


class ObjectIdField(serializers.Field):

    type_label = 'ObjectIdField'

    def to_representation(self, value):
        return smart_str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class BinaryField(serializers.Field):

    type_label = 'BinaryField'

    def __init__(self, **kwargs):
        try:
            self.max_bytes = kwargs.pop('max_bytes')
        except KeyError:
            #raise ValueError("BinaryField requires 'max_bytes' kwarg")
            self.max_bytes = 52428800
        super(BinaryField, self).__init__(**kwargs)

    def __set__(self, instance, value):
        """Handle bytearrays in python 3.1"""
        if PY3 and isinstance(value, bytearray):
            value = bin_type(value)
        return super(BinaryField, self).__set__(instance, value)

    def to_representation(self, value):
        return smart_str(value)

    def to_internal_value(self, data):
        if not isinstance(data, (bin_type, txt_type, Binary)):
            raise ValueError("BinaryField only accepts instances of "
                       "(%s, %s, Binary)" % (bin_type.__name__, txt_type.__name__))

        if self.max_bytes is not None and len(data) > self.max_bytes:
            raise ValueError('Binary value is too long')
        return  Binary(str(data))  #str thing somehow should not be here
