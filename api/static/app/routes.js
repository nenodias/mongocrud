app.config( ['$routeProvider','$locationProvider', function($routeProvider, $locationProvider) {

    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });

    $routeProvider

    .when('/', {
       templateUrl : 'static/app/views/home.html',
       controller     : 'HomeCtrl',
       access: {
         required: true
       }
    })

    .when('/login', {
       templateUrl : 'static/app/views/login.html',
       controller     : 'LoginCtrl',
       access: {
         required: false
       }
    })

    .when('/sobre', {
       templateUrl : 'static/app/views/sobre.html',
       controller  : 'SobreCtrl',
       access: {
         required: true
       }
    })

    .when('/contato', {
       templateUrl : 'static/app/views/contato.html',
       controller  : 'ContatoCtrl',
       access: {
         required: true
       }
    })

    .otherwise ({ redirectTo: '/' });
}]);

app.run(['$rootScope', '$location', '$cookieStore', '$http', function ($rootScope, $location, $cookieStore, $http) {
    $rootScope.globals = $cookieStore.get('globals') || {};
    console.log($rootScope.globals);

    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        if ($location.path() !== '/login' && !$rootScope.globals.currentUser) {
            $location.path('/login');
        }
    });

}]);
