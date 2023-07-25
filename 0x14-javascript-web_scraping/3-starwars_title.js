#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      try {
        const movie = JSON.parse(response.body);
        console.log(movie.title);
      } catch (parseError) {
        console.error(parseError);
      }
    } else {
      console.log(response.statusCode);
    }
  }
});
