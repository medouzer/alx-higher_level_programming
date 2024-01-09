#!/usr/bin/node

const { argv } = require('process');
let i = 0;
let j;
let nx;
let str;

nx = parseInt(argv[2]);

if (isNaN(nx)) console.log('Missing size');
else {
  while (i < nx) {
    j = 0;
    str = '';
    while (j < nx) {
      str += 'X';
      j++;
    }
    console.log(str);
    i++;
  }
}
