const { HOSTNAME, API } = require("../variables");

module.exports = function($scope, $timeout, $location, $window, Http){
    $scope.header = {
        "title": "Products",
        "createLink": "/#!/create"
    }

    $scope.form = {
        name: {type: "input", value: null},
        description: {type: "text", value: null},
    }

    $scope.data = [];

    $scope.init = function(){
        Http.sendGet("http://localhost:8000/product").then(
            function success(response){
                $scope.data = response.data;
            }
        )
    }
}