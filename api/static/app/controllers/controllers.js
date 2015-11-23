app.controller('HomeController', function ( $rootScope, $scope, $location, UsuarioEntry, LoginService) {
    /*
    var entry = UsuarioEntry.get({ id: $scope.id }, function() {
      console.log(entry);
    });
    */

    //var entries = UsuarioEntry.query({limit:2,offset:2},function() {//Filtrando e passanfo limite e offset, desde que os parâmetros estejam setados no resource

    var entries = UsuarioEntry.query({limit:2,offset:2},function() {
      $scope.usuarios = entries;
      console.log(entries);
    });

    /*
    $scope.entry = new UsuarioEntry();
    $scope.entry.nome = 'Horácio Dias';
    $scope.entry.senha = '123';
    $scope.entry.email = 'horacio.dias92@gmail.com';
    */

    /*
    UsuarioEntry.save($scope.entry, function() {
      //data saved. do something here.
    });
    */
});

app.controller('LoginController', function ( $rootScope, $scope, $location, LoginService) {
    $scope.email = "";
    $scope.senha = "";
    $scope.logon = function(){
      LoginService.logon($scope.email, $scope.senha);
    }
});


app.controller('SobreController', function( $rootScope, $scope, $location, LoginService){
});

app.controller('ContatoController', function( $rootScope, $scope, $location, LoginService){
});
