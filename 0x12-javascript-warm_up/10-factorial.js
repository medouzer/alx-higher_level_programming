#!/usr/bin/node

function factorial (num) {
  if (num <= 1) return 1;
  return num * factorial(num - 1);
}
const { argv } = require('process');
const num = parseInt(argv[2]);
if (isNaN(num)) console.log(1);
else console.log(factorial(num));
