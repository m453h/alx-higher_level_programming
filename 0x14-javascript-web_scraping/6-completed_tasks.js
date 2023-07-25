#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      try {
        const todos = JSON.parse(response.body);
        const data = {};

        for (const todo of todos) {
          const userId = todo.userId.toString();
          const status = todo.completed;

          if (!(userId in data)) {
            data[todo.userId.toString()] = 1;
          } else {
            if (status) {
              data[userId] = data[userId] + 1;
            }
          }
        }

        console.log(data);
      } catch (parseError) {
        console.error(parseError);
      }
    } else {
      console.log(response.statusCode);
    }
  }
});
