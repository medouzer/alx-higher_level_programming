#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, code) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log('code: ' + code.statusCode);
});
