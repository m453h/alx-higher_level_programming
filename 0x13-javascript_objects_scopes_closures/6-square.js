#!/usr/bin/node
const SquareBase = require('./5-square.js');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
};
