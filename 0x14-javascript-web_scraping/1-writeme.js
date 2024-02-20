#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const stringWrite = process.argv[3];

fs.writeFile(fileName, stringWrite, { encoding: 'utf8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
