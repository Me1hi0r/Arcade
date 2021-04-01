log = console.log

const MQTT_ADDR = "192.168.10.1";
const MQTT_PORT = 8080;
var clientId = `id_${parseInt(Math.random() * 1000)}`;
var client = new Messaging.Client(MQTT_ADDR, MQTT_PORT, clientId);

var options = {
    timeout: 3,
    onSuccess: function() {
        log(`MQTT: Connected: ${MQTT_ADDR}:${MQTT_PORT}, id: ${clientId}`);
        mqtt_subscribe('/er/player');
        mqtt_subscribe('/er/finish');
        mqtt_subscribe('/er/valid');
        mqtt_subscribe('/er/card');
    },
    onFailure: function(message) {
        log(`Error: MQTT: Connection: ${MQTT_ADDR}:${MQTT_PORT}:${message.errorMessage}`);
    }
};

client.onConnectionLost = function(responseObject) {
    alert(`Connection lost: Please, press OK, and wait for reboot ( ${responseObject.errorMessage} )`);
    location.reload();
};

client.onMessageArrived = function(message) {
    msg = message.payloadString;
    topic = message.destinationName;
    if(msg !== "no RFID available")
        msgs_check(topic, msg);
};

var mqtt_publish = function(payload, topic, _qos) {
    if (typeof _qos == "undefined") _qos = 2;
    var message = new Messaging.Message(payload);
    message.destinationName = topic;
    message.qos = _qos;
    client.send(message);
};

var mqtt_subscribe = function(topic, _qos) {
    if (typeof _qos == "undefined") _qos = 2;
    client.subscribe(topic, { qos: _qos });
};

var mqtt_connect = function() {
    client.connect(options);
};

var mqtt_disconnect = function() {
    client.disconnect();
};

mqtt_connect();

function select(name){
    return document.querySelector(name);
}


var isValid = true;
function err_msg(name, text){
    select(name).value = text;
    select(name).style.color = "red";
    isValid = false;
}

function val(name){
    return select(name).value;
}

function parseCpz(text){
    return parseInt(text.slice(3,-1).split(", 0x").join(""), 16);
}

function msgs_check(topic, msg) {
    log(`MQTT: Topic: ${topic}, Data: ${msg}`);

    //ADMIN
    if(topic === "/er/player"){
    // if(topic === "/er/card"){
        cpz_num = parseCpz(msg);
        select("#rfid").value = cpz_num;

        $.get(`check/${cpz_num}`, function(data, status){
            if(data == "new"){
                select("#card-title").innerText = "Добавить новую карту";
                select("#create_button").innerText = "Добавить";
                select("#name").value = "";
                select("#balance").value = "";
            } else {
                select("#create_button").innerText = "Изменить";
                select("#card-title").innerText = "Переопределить карту";
                let [name, balance, rfid] = data.split("|");
                select("#name").value = name;
                select("#balance").value = balance;
            }
        });
    }

    //GAME
    if(topic === "/er/valid"){
    // if(topic === "/er/player"){
        log("valid");
        let [name, cpz] = msg.split("|");
        let cpz_num = parseCpz(cpz);
        $.get(`balance/${cpz_num}`, function(data, status){
            log(data);
            if(data == "update")
                mqtt_publish( "activate", `/er/${name}/cmd`);
            if(data == "zero" || data == "none")
                mqtt_publish("invalid", `/er/${name}/cmd`);
        });
    }

    // RESULT
    if(topic === "/er/finish"){
    // if(topic === "/er/player"){
        let [riddle, cpz, points] = msg.split("|");
        $.post("result/",{
                csrfmiddlewaretoken: val('input[name="csrfmiddlewaretoken"]'),
                riddle: riddle,
                points: points,
                card: parseCpz(cpz)
            },(data, status) => log(data, data)
        );
    }
}

function sendData(){
    $.post("change/",{
            csrfmiddlewaretoken: val('input[name="csrfmiddlewaretoken"]'),
            name: val("#name"),
            balance: val("#balance"),
            card: val("#rfid")
        }, function(data, status){
            log(data);
            select("#card-title").innerText = "Карта изменена!";
            setTimeout(()=>{
                log("clear start screen");
                select("#card-title").innerText = "Приложите карту";
                select("#name").value = "";
                select("#balance").value = "0";
                select("#rfid").value = "";
                select("#create_button").innerText = "Создать/Изменить";
            }, 2000);
        });
}

function validateForm() {
    isValid = true;
    if(val("#name").includes(" ")) err_msg("#name", "В имени не должно быть пробелов");
    if(val("#name").length < 4) err_msg("#name", "Имя должно быть длинее 3 знаков");
    if(!parseInt(val("#balance"))) err_msg("#balance", "Введите число больше 0");
    if(val("#balance") < 1) err_msg("#balance", "Нулевой баланс");

    if(isValid) sendData();
    return false;
}
