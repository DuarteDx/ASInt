function sendPostRequest(url, data) {
    console.log('Starting ajax post request');

    return axios.post(url, {
        data,
        headers: {
            "Access-Control-Allow-Origin": "*"
        },
        responseType: 'json'
    })
        .then(function(response) {
            //console.log(response);
            console.log('[C]Server response:');
            console.log(response.data);
            return response.data;
        })
        .catch(function (error) {
            console.log(error);
            return 'An error occorred: ' + error;
        })
}



function sendGetRequestAxios(url) {
    console.log('Starting ajax get request for: ' + url);

    // Using a cors proxy to avoid cors block
    url = 'https://cors-anywhere.herokuapp.com/' + url;

    axios.get(url, {
        headers: {
            "Access-Control-Allow-Origin": '*'
        },
        responseType: 'json'
    })
      .then(function (response) {
        console.log(response.data);
        return response.data
      })
      .catch(function (error) {
        console.log(error);
      }) 
}

//Get latitute & longitude
function successFunction(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    //console.log('Your latitude is :'+lat+' and longitude is '+long);
    //Send user id and respective coordinates
    url = serverURL + "/sendLocation";
    sendPostRequest(url, {'user': dummyID,'location': {'latitude':lat, 'longitude':long}});
}

//Send user data to add him to DB
function addUserToDB(id , name) {
    url = serverURL + "/sendUserInfo";
    sendPostRequest(url, {'id': id,'name': name});
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }