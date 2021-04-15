const venom = require('venom-bot');
const axios = require('axios');

venom
  .create()
  .then((client) => start(client))
  .catch((erro) => {
    console.log(erro);
  });

function start(client) {
  client.onAnyMessage((message) => {
    const msgText = message.body.toUpperCase();
    if (msgText === 'LIST' && message.isGroupMsg === true && (message.chat.contact.name === "MercadoApp" || message.chat.contact.name === "Geladeira")) {
      axios.get('http://localhost:8000/list/')
      .then((response) => {
        resposta = "------------------LISTA------------------\n"
        response.data.Lista.forEach(element => {
          resposta = resposta + element["PRODUTO"] + " x"+element["QUANTIDADE"]+ "       € "+element["PREÇO"]+"\n"
        });
        resposta = resposta + "PREÇO TOTAL: "+ response.data["PREÇO"]+"\n"
        resposta = resposta + "-----------------------------------------------"

        client
        .sendText(message.from, resposta)
        .then((result) => {
          //console.log('Result: ', result); //return object success
        })
        .catch((erro) => {
          console.error('Error when sending: ', erro); //return object error
        });
      });
    }

    if (msgText.startsWith('ADD') && message.isGroupMsg === true && (message.chat.contact.name === "MercadoApp" || message.chat.contact.name === "Geladeira")) {
      const splited = msgText.split(" ")
      if(splited.length !== 3){
      }
      else{
        axios.post('http://localhost:8000/list/addToList/',{item:{id:splited[1]}, quantity:splited[2]})
        .then((response) => {
          client
          .sendText(message.from, "--->Item Added<---")
          .then((result) => {
            //console.log('Result: ', result); //return object success
          })
          .catch((erro) => {
            console.error('Error when sending: ', erro); //return object error
          });
        });
      }
    }

    if (msgText === 'PRODUCTS' && message.isGroupMsg === true && (message.chat.contact.name === "MercadoApp" || message.chat.contact.name === "Geladeira")) {
      axios.get('http://localhost:8000/products/shopList/')
      .then((response) => {
        resposta = "------------------PRODUTOS------------------\n"
        response.data.forEach(element => {
          resposta = resposta + element["name"] + " " + element["id"]+"\n"
        });
        resposta = resposta + "-----------------------------------------------"
        client
        .sendText(message.from, resposta)
        .then((result) => {
          //console.log('Result: ', result); //return object success
        })
        .catch((erro) => {
          console.error('Error when sending: ', erro); //return object error
        });
      });
    }

    if (message.body === 'CLEAR123' && message.isGroupMsg === true && message.chat.contact.name === "Geladeira") {
      axios.get('http://localhost:8000/list/clear/')
      .then((response) => {
        client
        .sendText(message.from, "--->LIST CLEARED<---")
        .then((result) => {
          //console.log('Result: ', result); //return object success
        })
        .catch((erro) => {
          console.error('Error when sending: ', erro); //return object error
        });
      });
    }
  });
}