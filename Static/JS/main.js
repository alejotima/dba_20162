var app = angular.module('myApp', ['ngRoute', 'ngResource']);
app.factory('Api', function($resource){
    return {
        User: $resource('api/users/:id',{
            id: '@id'
        })
    }
});
app.config(function ($routeProvider) {
    $routeProvider
    .when('/home', {
        templateUrl: '/static/views/home.html'
    })
    .when('/crud', {
        templateUrl: '/static/views/crud.html'
    })
});
app.controller('myCtrl', function ($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
});

app.controller('CrudCtrl', function ($scope, Api) {
    $scope.test = 'Esto es un prueba';
    $scope.users = Api.User.query();
    $scope.addUser = function(){
        console.log('esto es un agregar');
        $scope.newUser = {
            name: $scope.name,
            lastname: $scope.lastname
        };
        console.log($scope.newUser);
        Api.User.save($scope.newUser, function(data) {
            console.log(data);
            $scope.users = Api.User.query();
        });
    };
    $scope.removeUser = function(idnt){
        console.log('esete es el id a borrar - '+idnt);
        Api.User.delete({id:idnt},function(data){
            console.log(data);
            $scope.users = Api.User.query();
        });
    };
});