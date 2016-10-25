var app = angular.module('myApp', ['ngRoute']);
app.config(function ($routeProvider) {
    $routeProvider
    .when('/home', {
        templateUrl: '/static/home.html'
    })
    .when('/test', {
        templateUrl: '/static/home.html'
    })
});
app.controller('myCtrl', function ($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
});