#!/usr/bin/node
/* Script that prints the number of movies where
the character "Wedge Antilles" is present */
const request = require('request');
const url = process.argv[2];
request(url, function (err, res, body) {
  const wedge = 'https://swapi.co/api/people/18/';
  let count = 0;
  if (err) { console.log(err); } else {
    let result = JSON.parse(body).results;
    for (let i of result) {
      for (let j of i.characters) {
        if (j.indexOf(wedge) > -1) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
