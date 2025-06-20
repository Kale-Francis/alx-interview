#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie by movie ID
 * Usage: ./0-starwars_characters.js <Movie ID>
 */
const request = require('request');

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Function to fetch and print character names in order
  const fetchCharacter = (index) => {
    if (index >= characters.length) {
      return; // Done fetching all characters
    }

    request.get(characters[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }
      if (charResponse.statusCode !== 200) {
        console.error(`Error: Status code ${charResponse.statusCode} for character ${characters[index]}`);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  };

  // Start fetching characters from index 0
  fetchCharacter(0);
});
