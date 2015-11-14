app.factory('UsuarioEntry', ['$resource', function($resource) {
  return $resource('/api/usuarios/:id');
}]);

app.factory('LoginService', ['$rootScope', '$cookieStore', '$location', '$http' ,function($rootScope, $cookieStore, $location, $http) {
  var servico = {};
  servico.logon = function(email, senha){
    $http.post('/logon/',{"email":email, "senha":senha})
    .then(function successCallback(response) {
      //STATUS OK
      $rootScope.globals = {
        currentUser: {
            token: response.data.token
        }
      };
      $cookieStore.put('globals', $rootScope.globals);
      $location.path('/home');
      console.log("Foi pra home");
    }, function errorCallback(response) {
      //FAULT
      $rootScope.globals = {};
      $cookieStore.remove('globals');
    });
  }
  return servico;
}]);
