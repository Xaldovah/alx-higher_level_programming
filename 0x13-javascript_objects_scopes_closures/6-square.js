#!/usr/bin/node

const prevSquare = require('./5-square');

module.exports = class Square extends prevSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
