#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error Code:', response.statusCode);
    return;
  }

  const data = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (data[todo.userId] === undefined) {
        data[todo.userId] = 1;
      } else {
        data[todo.userId]++;
      }
    }
  });
  console.log(data);
});
