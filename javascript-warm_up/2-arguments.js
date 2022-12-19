#!/usr/bin/node
// use length function for use te arguments
const { argv } = require('process');

if (argv.length < 3) {
  console.log('No argument');
}

if (argv.length === 3) {
  console.log('Argument found');
}

if (argv.length > 3) {
  console.log('Arguments found');
}
