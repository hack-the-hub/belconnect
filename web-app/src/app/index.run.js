(function() {
  'use strict';

  angular
    .module('belconnect')
    .run(runBlock);

  /** @ngInject */
  function runBlock($log) {

    $log.debug('runBlock end');
  }

})();
