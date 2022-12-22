#!/usr/bin/node
// get the status code

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
const request = require('request');

request.get(url, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(data).title);
  }
});
