#!/usr/bin/node
// use argv for sarcha biggest integer in the list
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const args = argv.map(Number)
    .slice(2, argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
