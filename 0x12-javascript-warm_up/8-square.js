#!/usr/bin/node
let x = parseInt(process.argv[2]);

function square (num) {
  for (let i = 0; i < num; i++) {
    let string = '';
    for (let j = 0; j < num; j++) {
      string = string + 'X';
    }
    console.log(string);
  }
}
x ? square(x) : console.log('Missing size');
