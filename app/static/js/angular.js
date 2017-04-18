const app = angular.module("view_thumApp",[]);
app.controller("view_thumCtrl", function($scope, $window){
    $scope.urls=$window.urls;
    console.log("Angular");
    console.log($scope.urls);
    // $http.get("/api/thumbnails")
    // .then(function(response){
    //     $scope.urls = response.data.thumbnails;
    // }, function(response){
    //     $scope.urls = "Error: "+response;
    // });
});