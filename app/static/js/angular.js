const app = angular.module("view_thumApp",[]);
app.controller("view_thumCtrl", function($scope, $http){
    $http.get("/api/thumbnails")
    .then(function(response){
        $scope.urls = response.data.thumbnails;
    }, function(response){
        $scope.urls = "Error: "+response;
    });
});