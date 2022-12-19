#!/usr/bin/node
const { argv } = require('node:process');

if (argv[1] === 0) {
    console.log("No argument")
}

console.log("Argument found")
