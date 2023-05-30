var but = require('@amperka/button').connect(P0);

but.on('press', function() {
  console.log('button_is_pressed');
});

var sens = require('@amperka/thermometer').connect(A0);

setInterval(function(){
  var t = sens.read('C');
  console.log(t);
}, 500);

var but = require('@amperka/button').
  connect(P0, {
  holdTime: 1
});

var light = require('@amperka/light-sensor').connect(A0);
var temp = 0;

setInterval(function(){
  but.on('click', function() {
    console.log(1);
  });
  temp = light.read('lx');
  console.log(temp+'lx');
}, 10000);