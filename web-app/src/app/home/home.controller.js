(function() {
  'use strict';

  angular
    .module('belconnect')
    .controller('HomeController', HomeController);

  /** @ngInject */
  function HomeController($scope, $log, $http, Restangular, $stateParams, $state) {

    console.log('home dashboard');

    $scope.data = {
    availableOptions: [
      {id: '1', name: 'Category A'},
      {id: '2', name: 'Category B'},
      {id: '3', name: 'Category C'},
      {id: '4', name: 'Category D'}
    ],
    selectedOption: {id: '3', name: 'Category C'} //This sets the default value of the select in the ui
    };


    Restangular.all('belmeetings').getList().then(function(result) {
        $scope.belmeetings = result;
    });

    
  }
})();
