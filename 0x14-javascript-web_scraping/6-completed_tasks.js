#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const data = {};
      try {
        const todos = JSON.parse(response.body);

        if (typeof todos[Symbol.iterator] === 'function') {
          for (const todo of todos) {
            const userId = todo.userId;
            const status = todo.completed;
            if (status) {
              if (!(userId in data)) {
                data[userId] = 1;
              } else {
                data[userId] = data[userId] + 1;
              }
            }
          }
        }
      } catch (parseError) {
        console.error(parseError);
      }

      console.log(data);
    } else {
      console.log(response.statusCode);
    }
  }
});
