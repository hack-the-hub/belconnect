(function() {
  'use strict';

  angular
    .module('belconnect')
    .controller('SidebarController', SidebarController);

  /** @ngInject */
  function SidebarController($scope, $log) {



      angular.element('.dare-menu__has-submenu a').on( "click", function() {

        angular.element(this).parent().toggleClass('is-open');
        angular.element(this).parent().find('.dare-menu__submenu').slideToggle(600);
      });



  }
})();
