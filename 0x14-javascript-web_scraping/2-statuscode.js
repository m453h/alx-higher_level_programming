#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('Error occurred while making the GET request:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
