#!/usr/bin/node
// print argument in the third argv
const { argv } = require('process');

if (!argv[2]) {
  console.log('No argument');
}

if (argv[2]) {
  console.log(argv[2]);
}
