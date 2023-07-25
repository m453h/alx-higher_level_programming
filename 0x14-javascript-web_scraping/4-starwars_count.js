#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      let counter = 0;

      try {
        const movies = JSON.parse(response.body);
        for (const movie of movies.results) {
          for (const character of movie.characters) {
            if (character.includes('18')) {
              counter = counter + 1;
            }
          }
        }
      } catch (parseError) {
        console.error(parseError);
      }
      console.log(counter);
    } else {
      console.log(response.statusCode);
    }
  }
});
