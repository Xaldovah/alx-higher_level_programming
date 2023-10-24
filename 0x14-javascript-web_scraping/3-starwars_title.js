#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error('Error:', error);
  }
});
