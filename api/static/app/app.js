'use strict';

var app = angular.module('app',['ngRoute', 'ngResource', 'ngCookies']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('#{');
    $interpolateProvider.endSymbol('}#');
})




.run(['LoginService','$rootScope', '$cookieStore', '$location', '$http', '$route',
   function (LoginService, $rootScope, $cookieStore, $location, $http, $route) {
      if( !LoginService.permissao() ){
         $location.path('/login');
      }
   }]);

/*

//Funções auxiliares de CSRF
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/i.test(method))
}

function getCookie(name){
    var cookieValue = null;
    if(document.cookie && document.cookie != ''){
        var cookies = document.cookie.split(';');
        for( var i = 0; i < cookies.length; i++ ){
            var cookie = $.trim(cookies[i]);
            if(cookie.substring(0, name.length+1) == (name + '=') ) {
                cookieValue = decodeURIComponent( cookie.substring(name.length + 1) );
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxPrefilter( function (settings, originalOptions, xhr){
    var csrfToken;
    if(!csrfSafeMethod(settings.type) && !this.crossDomain){
        csrfToken = getCookie('csrfToken');
        xhr.setRequestHeader('X-CSRFToken',csrfToken);
    }
});

*/
