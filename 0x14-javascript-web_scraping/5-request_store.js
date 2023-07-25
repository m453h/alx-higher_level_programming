#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const content = response.body;
      fs.writeFile(filePath, content, 'utf-8', function (err, content) {
        if (err) {
          console.log(err);
        }
      });
    } else {
      console.log(response.statusCode);
    }
  }
});
