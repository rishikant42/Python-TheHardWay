// const axios = require('axios').default;

var app = new Vue({ 
    el: '#app',
    data: {
        message: 'Hello world!'
    },
      methods: {
          reverseMessage: function () {
              this.message = this.message.split('').reverse().join('')
          },
          getMsg: function() {
              axios.get('http://localhost:8000/app/home/').then((resp) => {
                  this.message = resp.data.name;
                  console.log(resp);
              });
          }
      }
});
