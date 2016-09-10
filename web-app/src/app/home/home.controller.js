(function() {
  'use strict';

  angular
    .module('belconnect')
    .controller('HomeController', HomeController);

  /** @ngInject */
  function HomeController($scope) {

    console.log('home dashboard');
  }
})();
