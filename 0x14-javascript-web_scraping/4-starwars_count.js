#!/usr/bin/node
/* Script that prints the number of movies where
the character "Wedge Antilles" is present */
const request = require('request');
let url = process.argv[2];
let wedge = 'https://swapi.co/api/people/18/';
request(url, function (err, res, body) {
  if (err) { console.log(err); }
  let response = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < response.length; i++) {
    let characters = response[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j] === wedge) {
        count += 1;
      }
    }
  }
  console.log(count);
});
