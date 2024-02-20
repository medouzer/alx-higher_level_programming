#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, code, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const users = {};
  for (const user of data) {
    if (user.completed) {
      if (users[user.userId]) {
        users[user.userId] += 1;
      } else {
        users[user.userId] = 1;
      }
    }
  }
  console.log(users);
});
