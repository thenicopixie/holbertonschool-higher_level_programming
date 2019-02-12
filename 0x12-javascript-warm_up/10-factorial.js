#!/usr/bin/node
let num = parseInt(process.argv[2]);
function fact (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
console.log(num ? fact(num) : 1);
