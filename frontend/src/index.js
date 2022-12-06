// Angularjs require
var angular = require("angular");
require("angular-route");
require("ng-file-upload");
require("angular-sanitize");


// AngularJS module working
var app = angular.module("App", ["ngRoute", "ngFileUpload", "ngSanitize"]);

app.config(function($interpolateProvider, $routeProvider) {
    // ____interpolate provider____
    $interpolateProvider.startSymbol("<%");
    $interpolateProvider.endSymbol("%>");

    $routeProvider.when("/", {
        templateUrl: "/src/pages/products.html",
        controller: "Products"
    }).when("/create", {
        templateUrl: "/src/pages/product-create.html",
        controller: "Products"
    }).when("/images", {
        templateUrl: "/src/pages/images.html",
        controller: "Images"
    }).when("/images/create", {
        templateUrl: "/src/pages/images-create.html",
        controller: "Images"
    });
});

// Factories
app.factory("Http", require("./manufactures/http"));

// Controllers app
app.controller("Products" , require("./controllers/products"));
app.controller("Images" , require("./controllers/images"));
