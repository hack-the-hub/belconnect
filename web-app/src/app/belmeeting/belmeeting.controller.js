(function() {
  'use strict';

  angular
    .module('belconnect')
    .controller('BelmeetingController', BelmeetingController);

  /** @ngInject */
  function BelmeetingController($scope, $log, $http, Restangular, $stateParams, $state) {


    $scope.belmeetingId = $stateParams.belmeetingId;



            var objId = $state.params; // has id, anotherParam, and yetAnotherParam
            var id = objId.belmeetingId;


        console.log('page loading completed');

        console.log('id: ' + id);

        var url = 'belmeetings/' + id;

        Restangular.oneUrl(url).get().then(function(result) {
            $scope.belmeeting = result;
        });




  }
})();
