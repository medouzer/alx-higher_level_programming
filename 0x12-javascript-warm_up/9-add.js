#!/usr/bin/ode
const { argv } = require('process');
const nb1 = parseInt(argv[2]);
const nb2 = parseInt(argv[3]);
function add(a, b) {
  return a + b;
}
console.log(add(nb1, nb2));
