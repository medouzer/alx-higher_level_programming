#!/usr/bin/node

function add(a, b) {
  return a + b;
}
const { argv } = require('process');
const nb1 = parseInt(argv[2]);
const nb2 = parseInt(argv[3]);
const sum = add(nb1, nb2);
console.log(sum);
