var GoogleMapsAPI = require('@googlemaps/google-maps=services-js');

const request = {
        query: "Museum of Contemporary Art Australia",
        fields: ["name", "geometry"],
};

service = new google.maps.places.PlacesService(map);
service.findPlaceFromQuery(request, (results, status) => {
    if (status === google.maps.places.PlacesServiceStatus.OK && results) {
        console.log(results)
    }

    console.log("YO")
});






// key: 'AIzaSyAhXsZryi0nqEHpjAspBzknmIk4XQFCkvs',
