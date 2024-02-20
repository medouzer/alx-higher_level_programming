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
  let flag = 0;
  for (const key in users) {
    if (flag === 0) {
      console.log(`{ '${key}': ${users[key]},`);
    } else if (flag === Object.keys(users).length - 1) {
      console.log(`  '${key}': ${users[key]} }`);
    } else {
      console.log(`  '${key}': ${users[key]},`);
    }
    flag++;
  }
});
