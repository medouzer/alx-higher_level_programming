#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (err, code, data) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(fileName, data, { encoding: 'utf8' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
