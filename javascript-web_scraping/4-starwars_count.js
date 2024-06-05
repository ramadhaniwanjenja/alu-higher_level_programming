#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(`/api/people/${wedgeId}/`)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
