#!/usr/bin/node

const Squareb = require('./5-square');

class Square extends Squareb {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
