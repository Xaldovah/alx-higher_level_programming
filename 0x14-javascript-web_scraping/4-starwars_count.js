#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

let times = 0;

request(movieId, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  const data = JSON.parse(body).results;

  data.forEach((film) => {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      times++;
    }
  });
  console.log(times);
});
