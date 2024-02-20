#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, { json: true }, (err, code, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.title);
});
