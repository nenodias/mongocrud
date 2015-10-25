app.controller('HomeCtrl', ['$rootScope','$scope', '$location', 'UsuariosService', function ($rootScope, $scope,$location, UsuariosService) {
    $rootScope.location_path = $location.path();
    UsuariosService.get({}, function (valores) {
        console.log(valores);
    })
}]);


app.controller('SobreCtrl', function($rootScope, $location)
{
   $rootScope.location_path = $location.path();
});

app.controller('ContatoCtrl', function($rootScope, $location)
{
   $rootScope.location_path = $location.path();
});
