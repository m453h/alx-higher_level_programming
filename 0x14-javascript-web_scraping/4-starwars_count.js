#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

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
        console.log(counter);
      } catch (parseError) {
        console.error(parseError);
      }
    } else {
      console.log(response.statusCode);
    }
  }
});