  // Create a client instance
    // client = new Paho.MQTT.Client("host", port,"client_id");
    var client = new Paho.MQTT.Client("m13.cloudmqtt.com", 31675, "web_" + parseInt(Math.random() * 100, 10));

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    var options = {
      useSSL: true,
      userName: "tbweb",
      password: "random",
      onSuccess:onConnect,
      onFailure:doFail
    }

    // connect the client
    client.connect(options);

    // called when the client connects
    function onConnect() {
      // Once a connection has been made, make a subscription and send a message.
      console.log("onConnect");
      client.subscribe("/CAR/IN");
      // message = new Paho.MQTT.Message("Hello CloudMQTT");
      // message.destinationName = "/LINE/REALTIME";
      // client.send(message);
    }

    function doFail(e){
      console.log(e);
    }

    // called when the client loses its connection
    function onConnectionLost(responseObject) {
      if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:"+responseObject.errorMessage);
      }
    }

    // called when a message arrives
    function onMessageArrived(message) {
      var strjson = $.parseJSON(message.payloadString);;
      console.log("On Message: " + strjson["id"]);
      $("#tb-title").html("Car ID: " + strjson["id"]);
      $("#tb-img").attr('src',strjson["pic"]);
      $("#tb-driver").html(strjson["driver"]);
      $("#tb-datetime").html(strjson["timestamp"]);
      $("#tb-price").html(strjson["fee"]);
      if(strjson["id"] != "Car not found") {
        $("#tb-submit").prop("disabled", false);
      }
    }

    $("#tb-submit").click(function() {
      alert($("#tb-title").html() + ' is paid!');
      message = new Paho.MQTT.Message($("#tb-title").html());
      message.destinationName = "/CAR/RES";
      client.send(message);
      $("#tb-submit").prop("disabled", true);
    });
