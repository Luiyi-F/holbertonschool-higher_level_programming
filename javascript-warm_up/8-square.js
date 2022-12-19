#!/usr/bin/node
// use argv and nasted loop for print square
const { argv } = require('process');
const num = parseInt(argv[2]);

if (!num) {
  console.log('Missing size');
}
for (let index1 = 0; index1 < num; index1++) {
  for (let index2 = 0; index2 < num; index2++) {
    process.stdout.write('X');
  }
  console.log('');
}
