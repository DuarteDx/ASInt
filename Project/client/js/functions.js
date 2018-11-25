function sendPostRequest(url) {
    console.log('batatas');

    axios.post(url, {
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