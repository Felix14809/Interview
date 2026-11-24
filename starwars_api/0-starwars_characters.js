#!/usr/bin/node

const movie  = process.argv[2];
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${movie}`, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  
  const characters = JSON.parse(body).characters;
  const charNames = [];
  let checked = 0

  characters.forEach((charUrl, i) => {
    request(charUrl, (error, response, body) => {
         if (error) {
        console.log(error);
        return;
        }

        charNames[i] = JSON.parse(body).name;
        checked++;

        if (checked === characters.length) {
            console.log(charNames.join('\n'));
        }
    });
  });
});
