#!/usr/bin/node
let len = process.argv.length;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).sort();
  console.log(args[args.length - 2]);
}
