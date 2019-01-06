var serverURL = "http://127.0.0.1:5000";
const dummyID = 81356;

var userName;
var userId;

var authCode = getAuthCode();
    getTokens(authCode).then(data => {
        var accessToken = data['access_token'];
        var refreshToken = data['refresh_token'];
        console.log(accessToken);
        console.log(refreshToken);
        getUserInfo(accessToken, refreshToken).then(userData => {
            userName = userData['name'];
            userName = userName.split(' ');
            userName = userName[0] + ' ' + userName[userName.length-1];
            userId = userData['username'];
            console.log('Username: ' + userName);
            console.log('User id: ' + userId);
            addUserToDB(userId, userName);
        });
    });

var sendLocation = new Vue({
  el: '#sendLocation',
  data: {
    locationSentCounter: 0,
    locationSentLast: 'nothing sent'
  },
  created() {
    setTimeout(() => this.userName = userName, 3000);
    setTimeout(() => this.userId = userId, 3000);
    this.interval = setInterval(this.handleSubmit, 2000);
  },
  methods: {
    handleSubmit() {
      this.locationSentCounter += 1;

      var currentdate = new Date();
      this.locationSentLast = currentdate.getHours() + ":"  
                              + currentdate.getMinutes() + ":" 
                              + currentdate.getSeconds();

      //Get latitute and longitude and send it to server (ajax request done inside getCurrentPosition())
      if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(successFunction, console.log('error in getting location'));
      } else {
          alert('[C]It seems like Geolocation, which is required for this page, is not enabled in your browser. Please use a browser which supports it.');
      }

    }
  }
})

var userInfo = new Vue({
  el: '#userInfo',
  data: {
    userId: '',
    userName: ''
  },
  created() {
    setTimeout(() => this.userName = userName, 2500);
    setTimeout(() => this.userId = userId, 2500);
  }
})

var sendRange = new Vue({
  el: '#sendRange',
  data: {
    range: '',
  },
  created() {
    setTimeout(() => this.userName = userName, 2500);
    setTimeout(() => this.userId = userId, 2500);
  },
  methods: {
    handleSubmit() {
      url = serverURL + '/defineRange';
      sendPostRequest(url, {'user':userId, 'range':this.range});
      console.log('[C]Range sent: ' + this.range);
    }
  }
})

var sendMessage = new Vue({
  el: '#sendMessage',
  data: {
    userMessage: '',
  },
  created() {
    setTimeout(() => this.userName = userName, 2500);
    setTimeout(() => this.userId = userId, 2500);
  },
  methods: {
    handleSubmit() {
      url = serverURL + '/broadcastClientMessage';
      sendPostRequest(url, {'user':userId,'message':this.userMessage});
      console.log('[C]Message sent: ' + this.userMessage);
    }
  }
})

var getNearbyUsers = new Vue({
  el: '#getNearbyUsers',
  data: {
    nearbyUsersList: [],
  },
  created() {
    setTimeout(() => this.userName = userName, 2500);
    setTimeout(() => this.userId = userId, 2500);
    this.interval = setInterval(this.getListOfNearbyUsers, 2000);
  },
  methods: {
    getListOfNearbyUsers() {
      //ToDo: Ajax code to get list of users
      url = serverURL + '/getPeopleInRange';
      sendPostRequest(url, {'user':userId}, this.nearbyUsersList).then(data => this.nearbyUsersList = data);
      console.log('[C]Requested nearbyUsersList for ' + userId);
      
      console.log('[C]get users button pressed');
      console.log(this.nearbyUsersList);
    }
  }
})

var getMessages = new Vue({
  el: '#getMessages',
  data: {
    messageList: [],
  },
  created() {
    setTimeout(() => this.userName = userName, 2500);
    setTimeout(() => this.userId = userId, 2500);
    this.interval = setInterval(this.getListOfMessages, 2000);
  },
  methods: {
    getListOfMessages() {
      //ToDo: Ajax code to get list of messages
      url = serverURL + '/getUserMessages';
      sendPostRequest(url, {'user':userId}).then(data => this.messageList = data);
      console.log('[C]Requested list of messages for ' + userId);

      console.log('[C]get messages button pressed');
      this.messageListDummy = [{from: 'Duarte', content: 'Oi, tudo bem?'},
                          {from: 'BotSDEEC', content: 'Não baloiçar nas cadeiras!'},
                          {from: 'ISTPress', content: 'Notícia de última hora: grupo de alunos sobredotados tiram 20 na cadeira de ASint!'}
                        ];
    }
  }
})









//AUTH FUNCTIONS

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