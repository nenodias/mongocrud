app.config( ['$routeProvider','$locationProvider', function($routeProvider, $locationProvider) {

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });

    $routeProvider
    .when('/', {
       templateUrl : 'static/app/views/home.html',
       controller     : 'HomeController',
       acesso: {
         requerido: true
       }
    })

    .when('/login', {
       templateUrl : 'static/app/views/login.html',
       controller     : 'LoginController'
    })

    .when('/sobre', {
       templateUrl : 'static/app/views/sobre.html',
       controller  : 'SobreController',
       acesso: {
         requerido: true
       }
    })

    .when('/contato', {
       templateUrl : 'static/app/views/contato.html',
       controller  : 'ContatoController',
       acesso: {
         requerido: true
       }
    })

    .otherwise ({ redirectTo: '/' });
}]);
