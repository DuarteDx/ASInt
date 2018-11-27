function sendPostRequest(url, data) {
    console.log('batatas');

    axios.post(url, {
        data,
        headers: {
            "Access-Control-Allow-Origin": "localhost"
        },
        responseType: 'json'
    })
        .then(function(response) {
            console.log(response);
            quote.textContent = response.data[0];
        })
        .catch(function (error) {
            console.log(error);
        })
}

//Get latitute & longitude
function successFunction(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    console.log('Your latitude is :'+lat+' and longitude is '+long);
    //Send user id and respective coordinates
    url = serverURL + "/sendLocation";
    sendPostRequest(url, {'user': '81356','location': {'latitude':lat, 'longitude':long}});
}