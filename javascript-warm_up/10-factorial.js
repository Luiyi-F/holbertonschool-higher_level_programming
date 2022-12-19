#!/usr/bin/node
// use argv for create a factorial number
const { argv } = require('process');
const num = parseInt(argv[2]);

console.log(factorial(num));

function factorial(n) {
  if (!n)
    return 1;

  return n * factorial(n - 1);
}
