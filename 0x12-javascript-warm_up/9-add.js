#!/usr/bin/node

function add(a, b) {
  return a + b;
}
const { argv } = require('process');
const nb1 = parseInt(argv[2], 10);
const nb2 = parseInt(argv[3], 10);
console.log(add(nb1, nb2));
