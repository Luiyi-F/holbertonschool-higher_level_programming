#!/usr/bin/node
// use argv and the function for create add function
const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

add(num1, num2);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
