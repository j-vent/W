$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})


function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
        center: {lat: 53.558928395132305, lng:  -113.49684146004718}
    });
    directionsDisplay.setMap(map);
    // calculateAndDisplayRoute(directionsService, directionsDisplay);

}