(function() {
  'use strict';

  angular
    .module('belconnect')
    .controller('HomeController', HomeController);

  /** @ngInject */
  function HomeController($scope, $log, $http, Restangular, $stateParams) {

    console.log('home dashboard');

    Restangular.all('belstops').getList().then(function(result) {
        $scope.belstops = result;
    });

    $scope.belstopId = $stateParams.belstopId;
  }
})();
