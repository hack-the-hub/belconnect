(function() {
  'use strict';

  angular
    .module('belconnect')
    .config(routerConfig);

  /** @ngInject */
  function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'app/main/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .state('dashboard', {
        abstract: true,
          url: '/dashboard',
          views: {
              '@': {
                  templateUrl: 'app/dashboard/dashboard.html',
                  controller: 'HomeController',
                  controllerAs: 'home'
              }
          }
      })
      .state('dashboard.home', {
          url: '/home',
          views: {
              'main@dashboard': {
                  templateUrl: 'app/home/home.html',
              }
          }
      });

    $urlRouterProvider.otherwise('/');
  }

})();
