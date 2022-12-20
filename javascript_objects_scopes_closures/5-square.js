#!/usr/bin/node
// create a class named square with inherits from
// rectangle
const Rectangle = require('./4-rectangle');

module.exports = class square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
