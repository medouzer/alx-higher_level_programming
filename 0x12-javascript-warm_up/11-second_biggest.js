#!/usr/bin/node

const { argv } = require('process');
if (argv.length <= 3) console.log(0);
else {
  const args = argv.slice(2).sort((a, b) => b - a);
  console.log(args[1]);
}
