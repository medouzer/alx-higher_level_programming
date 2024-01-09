#!/usr/bin/node

function add(a, b) {
  return a + b;
}
const { argv } = require('process');

let a = parseInt(argv[2]);
let b = parseInt(argv[3]);

console.log(add(a, b));
