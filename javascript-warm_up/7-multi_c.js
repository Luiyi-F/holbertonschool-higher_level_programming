#!/usr/bin/node
// use argv by n times for print
const { argv } = require('process');
const num = parseInt(argv[2]);

if (!num) {
  console.log('Missing number of occurrences');
}

for (let index = 0; index < num; index++) {
  console.log('C is fun');
}
