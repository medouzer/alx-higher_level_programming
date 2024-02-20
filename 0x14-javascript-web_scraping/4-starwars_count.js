#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, code, data) => {
  if (err) {
    console.error(err);
    return;
  }
  let count = 0;
  console.log(code.statusCode);
  const results = data.results;
  results.forEach((film) => {
    if (
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ) {
      count++;
    }
  });
  console.log(count);
});
