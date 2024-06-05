const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from command-line arguments

// Make a GET request to the Star Wars API endpoint for films
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data:', response.statusMessage);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Iterate over the characters list and print each character name
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data:', response.statusMessage);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
