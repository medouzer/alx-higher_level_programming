#!/usr/bin/node

const { argv } = require('process');
let i;

if (argv.length <= 2) console.log('Missing number of occurrences');
else i = parseInt(argv[2]);

while (i > 0) {
  console.log('C is fun');
  i--;
}
