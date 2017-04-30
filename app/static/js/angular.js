const app = angular.module("view_thumApp",[]);
app.controller("view_thumCtrl", function($scope, $http){
    console.log("SOEM")
 $http.get("/url")
    .then(function(response){
        $scope.urls = response.data.imag; 
        console.log('RESPONSE');
        console.log($scope.urls);
    }, function(response){
        $scope.urls = "Error: "+response;
    });
});
