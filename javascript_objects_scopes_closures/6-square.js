#!/usr/bin/node
// create function for print the size with diferent char
const Rectangle = require('./5-square');

module.exports = class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    }

    if (c) {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
