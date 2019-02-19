#!/usr/bin/node
/* Script that prints the number of movies where
the character "Wedge Antilles" is present */
const request = require('request');
let url = process.argv[2];
let wedge = 'https://swapi.co/api/people/18/';
request.get(url, function (err, res, body) {
  if (err) { console.log(err); }
  let people = JSON.parse(body).results[0].characters;
  for (let i = 0; i < people.length; i++) {
    if (people[i] === wedge) {
      request.get(people[i], function (err, res, body) {
        if (err) { console.log(err); }
        let wA = JSON.parse(body).films;
        console.log(wA.length);
      });
    }
  }
});
