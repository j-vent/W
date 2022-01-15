$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + "AIzaSyAuAwyUS_LqCs0uSfMIewefuSSllj2fD7A" + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)

})


function initMap() {
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 10,
        center: {lat: 53.558928395122305, lng:  -113.49684146004718}
    });
    directionsDisplay.setMap(map);
    // calculateAndDisplayRoute(directionsService, directionsDisplay);

}

