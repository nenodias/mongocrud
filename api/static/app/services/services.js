app.factory('UsuarioEntry', ['$resource', function($resource) {
  return $resource('/api/usuarios/:id');
}]);
