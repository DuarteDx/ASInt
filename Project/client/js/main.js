var sendLocation = new Vue({
    el: '#sendLocation',
    data: {
      locationSentCounter: 0,
      locationSentLast: 'xxx'
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
      this.nearbyUsersList = [{name: 'Lourenço'}];
    }
  }
})