var serverURL = "http://127.0.0.1:5000";
const dummyID = 81356;

var sendLocation = new Vue({
  el: '#sendLocation',
  data: {
    locationSentCounter: 0,
    locationSentLast: 'nothing sent'
  },
  created() {
    //this.interval = setInterval(this.handleSubmit, 2000)
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
    userId: '81356',
    userName: 'Lourenço Pato'
  },
  methods: {
  }
})

var sendRange = new Vue({
  el: '#sendRange',
  data: {
    range: '',
  },
  methods: {
    handleSubmit() {
      url = serverURL + '/defineRange';
      sendPostRequest(url, {'user':dummyID, 'range':this.range});
      console.log('[C]Range sent: ' + this.range);
    }
  }
})

var sendMessage = new Vue({
  el: '#sendMessage',
  data: {
    userMessage: '',
  },
  methods: {
    handleSubmit() {
      url = serverURL + '/broadcastClientMessage';
      sendPostRequest(url, {'user':dummyID,'message':this.userMessage});
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
    //this.interval = setInterval(this.getListOfNearbyUsers, 2000)
  },
  methods: {
    getListOfNearbyUsers() {
      //ToDo: Ajax code to get list of users
      url = serverURL + '/getPeopleInRange';
      sendPostRequest(url, {'user':dummyID}, this.nearbyUsersList).then(data => this.nearbyUsersList = data);
      console.log('[C]Requested nearbyUsersList for ' + dummyID);
      
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
    //this.interval = setInterval(this.getListOfMessages, 2000)
  },
  methods: {
    getListOfMessages() {
      //ToDo: Ajax code to get list of messages
      url = serverURL + '/getUserMessages';
      sendPostRequest(url, {'user':dummyID}).then(data => this.messageList = data);
      console.log('[C]Requested list of messages for ' + dummyID);

      console.log('[C]get messages button pressed');
      this.messageListDummy = [{from: 'Duarte', content: 'Oi, tudo bem?'},
                          {from: 'BotSDEEC', content: 'Não baloiçar nas cadeiras!'},
                          {from: 'ISTPress', content: 'Notícia de última hora: grupo de alunos sobredotados tiram 20 na cadeira de ASint!'}
                        ];
    }
  }
})