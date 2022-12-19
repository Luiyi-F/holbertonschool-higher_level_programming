#!/usr/bin/node
// use parserInt for change type of arguments
const { argv } = require('process');
const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
