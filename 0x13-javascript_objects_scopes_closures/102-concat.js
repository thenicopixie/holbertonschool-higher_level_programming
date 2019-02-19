#!/usr/bin/node
/* Script that concats 2 files */
const fs = require('fs');
let contents = fs.readFileSync(process.argv[2], 'utf8');
contents += fs.readFileSync(process.argv[3], 'utf8');
fs.writeFile(process.argv[4], contents);
