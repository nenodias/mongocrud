app.config( ['$routeProvider','$locationProvider', function($routeProvider, $locationProvider) {

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });

    $routeProvider

    .when('/', {
       templateUrl : 'static/app/views/home.html',
       controller     : 'HomeCtrl',
    })

    .when('/login', {
       templateUrl : 'static/app/views/login.html',
       controller     : 'LoginCtrl',
    })

    .when('/sobre', {
       templateUrl : 'static/app/views/sobre.html',
       controller  : 'SobreCtrl',
    })

    .when('/contato', {
       templateUrl : 'static/app/views/contato.html',
       controller  : 'ContatoCtrl',
    })

    .otherwise ({ redirectTo: '/' });
}]);
