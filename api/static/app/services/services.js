app.factory('UsuarioEntry', ['$resource', function($resource) {
  return $resource('/api/usuarios/:id');
}]);

app.factory('LoginService', ['$rootScope', '$cookieStore', '$location', '$http', '$route',
function($rootScope, $cookieStore, $location, $http, $route) {
    var servico = {};

    servico.logoff = function(){
      $rootScope.globals = {};
      $cookieStore.remove('globals');
      $rootScope.logged = false;
    };

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
          servico.logoff();
      });
    };

     servico.permissao = function(){
         $rootScope.location_path = $location.path();
         var permissao_necessaria = false;
         $rootScope.logged = false;
         try{
           if ($cookieStore.get('globals') !== undefined && $cookieStore.get('globals').currentUser !== undefined){
             $rootScope.globals = $cookieStore.get('globals');
           }
           permissao_necessaria = $route.current.acesso.requerido;
         }catch(exx){}
         if ( $rootScope.globals !== undefined && $rootScope.globals.currentUser !== undefined ){
             $rootScope.logged = true;
             console.log("Ok  autenticacao");
             return true;
         }else if ( permissao_necessaria ) {
             console.log("Falha de autenticacao");
             return false;
         }
     };
     return servico;
}]);
