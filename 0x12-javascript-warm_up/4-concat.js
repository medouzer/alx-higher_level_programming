#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 2) console.log('undefined is undefined');
else if (argv.length === 3) console.log(argv[2], ' is undefined');
else if (argv.length === 4) console.log(argv[2], ' is ', argv[3]);
