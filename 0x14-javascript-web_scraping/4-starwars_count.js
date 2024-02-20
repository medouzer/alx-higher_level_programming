#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, code, data) => {
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    const results = data.results;
    for (const film of results) {
      const filmschar = film.characters;
      for (const charf of filmschar) {
        if (charf.includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
