#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const data = {};
      const todos = JSON.parse(response.body);

      for (const i in todos) {
        const todo = todos[i];
        if (todo.completed === true) {
          if (data[todo.userId] === undefined) {
            data[todo.userId] = 1;
          } else {
            data[todo.userId]++;
          }
        }
      }

      console.log(data);
    } else {
      console.log(response.statusCode);
    }
  }
});
