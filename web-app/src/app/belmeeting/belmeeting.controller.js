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
        var urlCat = 'categories';


        Restangular.oneUrl(url).get().then(function(result) {
            $scope.belmeeting = result;
        });

        $scope.categories = {
          '1': 'culture',
          '2': 'sports',
          '3': 'tech',
          '4': 'culture',
          '5': 'music'
        }





  }
})();
