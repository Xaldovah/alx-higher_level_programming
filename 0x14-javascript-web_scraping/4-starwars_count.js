#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: 4-starwars_count.js <API_URL>');
  process.exit(1);
}

let times = 0;

request(movieId, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  try {
    const data = JSON.parse(body).results;

    data.forEach((film) => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        times++;
      }
    });

    console.log(times);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    process.exit(1);
  }
});
