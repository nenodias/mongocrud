app.factory('UsuariosService', ['$resource', function($resource) {
  return $resource('/api/usuarios', {}, {
      query: {
          method: 'GET',
          params: {},
          isArray: false
      }
  });
}]);
