#!/usr/bin/node
// create script for read a file

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, (error, data)) => {
  if (!error) {
    console.log(data.toString());
  }
  console.log(error);
}
