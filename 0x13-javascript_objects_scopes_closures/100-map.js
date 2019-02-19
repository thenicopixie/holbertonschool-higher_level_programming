#!/usr/bin/node
/* Script that imports an array and computes a new array */
const a_list = require('./100-data.js').list
let i = 0;
const new_list = a_list.map(function(num) {
return num * i++;
});
console.log(a_list);
console.log(new_list);
