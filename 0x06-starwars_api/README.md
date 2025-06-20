0x06. Star Wars API
Project Overview
   This project, part of the ALX interview preparation, involves fetching and displaying Star Wars character names from a specified movie using the Star Wars API (SWAPI). The script uses Node.js and the request module to make HTTP requests and processes command-line arguments to determine the movie ID.
Requirements

Environment: Ubuntu 20.04 LTS
Node.js Version: 10.14.x
Allowed Editors: vi, vim, emacs
Code Style: semistandard (Standard + semicolons, Airbnb style)
Files: Must be executable, start with #!/usr/bin/node, and end with a newline
Dependencies: request module

Task Description
Task 0: Star Wars Characters

File: 0-starwars_characters.js
Description: Fetches and prints all character names from a Star Wars movie specified by its ID.
Usage: ./0-starwars_characters.js <Movie ID>
Example: ./0-starwars_characters.js 3 for “Return of the Jedi”.
Prints one character name per line, in the order of the characters list in the /films/<ID> endpoint.


API: https://swapi-api.alx-tools.com/api/

Setup and Usage

Install Node.js 10:curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs


Install Dependencies:sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules


Clone the Repository:git clone <your-repo-url>
cd alx-interview/0x06-starwars_api


Make File Executable:chmod +x 0-starwars_characters.js


Run the Script:./0-starwars_characters.js 3

Example output:Luke Skywalker
C-3PO
R2-D2
...



Files

0-starwars_characters.js: Script to fetch and print character names.
README.md: This file, describing the project and usage.

Author
   [Kale Francis]
License
   This project is for educational purposes as part of the ALX program.
