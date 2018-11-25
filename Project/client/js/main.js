var serverURL = "http://127.0.0.1:5000";

var sendLocation = new Vue({
  el: '#sendLocation',
  data: {
    locationSentCounter: 0,
    locationSentLast: 'nothing sent'
  },
  methods: {
    handleSubmit() {
      this.locationSentCounter += 1;

      var currentdate = new Date();
      this.locationSentLast = currentdate.getHours() + ":"  
                              + currentdate.getMinutes() + ":" 
                              + currentdate.getSeconds();

      url = serverURL + "/sendLocation";
      sendPostRequest(url);
    }
  }
})

var sendRange = new Vue({
  el: '#sendRange',
  data: {
    range: '',
  },
  methods: {
    handleSubmit() {
      //ToDo: Ajax code to send message
      console.log('Range sent: ' + this.range);
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
      //ToDo: Ajax code to send message
      console.log('Message sent: ' + this.userMessage);
    }
  }
})

var getNearbyUsers = new Vue({
  el: '#getNearbyUsers',
  data: {
    nearbyUsersList: [],
  },
  methods: {
    getListOfNearbyUsers() {
      //ToDo: Ajax code to get list of users
      console.log('get users button pressed');
      this.nearbyUsersList = [{name: 'Lourenço Pato'},
                              {name: 'José Peres'}, 
                              {name: 'Francisco Azevedo'}
                            ];
    }
  }
})

var getMessages = new Vue({
  el: '#getMessages',
  data: {
    messageList: [],
  },
  methods: {
    getListOfMessages() {
      //ToDo: Ajax code to get list of messages
      console.log('get messages button pressed');
      this.messageList = [{from: 'Duarte', content: 'Oi, tudo bem?'},
                          {from: 'BotSDEEC', content: 'Não baloiçar nas cadeiras!'},
                          {from: 'ISTPress', content: 'Notícia de última hora: grupo de alunos sobredotados tiram 20 na cadeira de ASint!'}
                        ];
    }
  }
})