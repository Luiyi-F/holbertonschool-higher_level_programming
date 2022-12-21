#!/usr/bin/node
// scrit for write in other file

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, (error) => {
  if (error) console.log(error);
});
