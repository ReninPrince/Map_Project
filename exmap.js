// function initMap() {
//   // The location of Uluru
//   var place = {lat: 13.0827, lng: 80.2707};
//   var place1 = ['salem']
//   // The map, centered at Uluru
//   var map = new google.maps.Map(
//       document.getElementById('map'), {zoom: 8, center: place});
//   // The marker, positioned at Uluru
//   var marker = new google.maps.Marker({position: place, map: map,animation:google.maps.Animation.BOUNCE});
// }
function initAutocomplete() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 8,
          center: {lat: 13.0827, lng: 80.2707}
        });
        var geocoder = new google.maps.Geocoder();

        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map);
        });
      }

      function geocodeAddress(geocoder, resultsMap) {
        var address = document.getElementById('address').value;
        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
              map: resultsMap,
              zoom: 12,
              animation:google.maps.Animation.BOUNCE,
              position: results[0].geometry.location
            });
          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      }
