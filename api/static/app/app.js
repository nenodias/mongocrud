var app = angular.module('app',['ngRoute', 'ngResource']);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('#{');
    $interpolateProvider.endSymbol('}#');
});
