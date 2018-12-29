function getAuthCode() {
    var pageUrl = window.location.search.substring(1);
    var dividedUrl = pageUrl.split('=');
    console.log(dividedUrl[1]);
    return dividedUrl[1];
}

function getTokens(authCode) {
    url = 'https://cors-anywhere.herokuapp.com/https://fenix.tecnico.ulisboa.pt/oauth/access_token?client_id=570015174623324&client_secret=dhhc25DQrqlMtglcB7UpC4tpYOQhqSp2c4Lx7ZI7YqfEqIDSbCnlSpZrerAdTvQv74UXTCQIjXtkhpw/1O8Djg==&redirect_uri=http://127.0.0.1&code=' + authCode + '&grant_type=authorization_code';
    return axios.post(url)
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

function getUserInfo(accessToken, refreshToken) {
    url = 'https://cors-anywhere.herokuapp.com/https://fenix.tecnico.ulisboa.pt/api/fenix/v1/person?access_token=' + accessToken + '&refresh_token=' + refreshToken;
    return axios.get(url)
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