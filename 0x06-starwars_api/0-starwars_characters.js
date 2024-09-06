#!/usr/bin/node
/*
    Write a script that prints all characters of a Star Wars movie:
    1- base url = https://swapi-api.alx-tools.com/api/
    2- then use first argumrnt to get the required film url=https://swapi-api.alx-tools.com/api/films/arg1
    3- get chracters key of the json of prev request
    3- iterate over the characters's value list and send a get request to each item
    4- get the value of the key name for each request to a chracter url
 */
const request = require('request');
var characters_names = [];
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, async function (error, response, body) {
  if (error) {
    print(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            print(error);
          } else {
            characters_names.push(JSON.parse(body).name);
          }
          resolve();
        });
      });
    }
  }
});
var i = 0;
for (i = 0; i < characters_names.length; i++){
    print(characters_names[i]);
}