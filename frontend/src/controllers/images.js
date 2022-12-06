const { HOSTNAME, API } = require("../variables");

module.exports = function($scope, $timeout, $location, $window, Http){
    $scope.header = {
        "title": "Images",
        "createLink": "/#!/images/create"
    }

    $scope.form = {
        upload: {type: "upload", value: null},
    }
}