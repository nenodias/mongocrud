app.factory('UsuarioEntry', ['$resource', function($resource) {
  return $resource('/api/usuarios/:id');
}]);

app.factory('LoginService', ['$rootScope', '$cookieStore', '$location', '$http', '$route',
function($rootScope, $cookieStore, $location, $http, $route) {
    var servico = {};

    servico.logon = function(email, senha){
      $http.post('/logon/',{"email":email, "senha":senha})
      .then(function successCallback(response) {
          $rootScope.globals = {
            currentUser: {
                token: response.data.token
            }
          };
          $cookieStore.put('globals', $rootScope.globals);
          $location.path('/home');
      }, function errorCallback(response) {
          //FAULT
          $rootScope.globals = {};
          $cookieStore.remove('globals');
      });
    };

     servico.permissao = function($scope){
         $scope.location_path = $location.path();
         var acesso = false;
         $rootScope.logged = false;
         try{
             acesso = $route.current.acesso.requerido;
         }catch(exx){}
         if ( $rootScope.globals !== undefined && $rootScope.globals.currentUser !== undefined ){
             $rootScope.logged = true;
             console.log("Ok  autenticacao");
         }else if ( acesso ) {
             $location.path('/login');
             console.log("Falha de autenticacao");
         }
     };
     return servico;
}]);
