#!/usr/bin/node

const { argv } = require('process');
const nx = parseInt(argv[2]);

if (!isNaN(nx)) {
  for (let i = 0; i < nx; i++) {
    let str = '';
    for (let j = 0; j < nx; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
