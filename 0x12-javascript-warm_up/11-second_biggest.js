#!/usr/bin/node
let len = process.argv.length;

function sorted(a, b) {
  return (a - b);
}
if (len === 2 || len === 3) {
  console.log(0);
} else {
  let args = process.argv.slice(2).sort(sorted);
  console.log(args[args.length - 2]);
}
