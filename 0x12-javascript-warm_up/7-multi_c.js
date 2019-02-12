#!/usr/bin/node
let x = parseInt(process.argv[2]);
function c(num) {
  while(num > 0) {
    console.log('C is fun');
    num--;
  }
}
isNaN(x) ? console.log('Missing number of occurrences') : c(x);
