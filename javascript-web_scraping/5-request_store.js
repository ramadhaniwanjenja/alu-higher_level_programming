#!/usr/bin/node
const request = require('request');

const fs = require('fs');

const url = process.argv[2];

const filePath = process.argv[3];

request.get(url, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, res.body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
