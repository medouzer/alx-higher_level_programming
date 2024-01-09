#!/usr/bin/node

const { argv } = require('process');

const convertedNumber = parseInt(argv[2]);

if (!isNaN(convertedNumber)) console.log(`My number: ${convertedNumber}`);
else console.log('Not a number');
