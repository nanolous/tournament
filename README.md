<b>Udacity Database Project<b>

This project is a tournament game engine.

It effectively exercies SQL to create the DB structure, players, matches, and more.

Postgresql and Psycopg2 are the tools for development.

Setup:<br>
0. Download the tournament zip file
1. Extract the zip file to a directory
2. Launch a command prompt
3. Navigate to the zip file directory
4. Launch psql utility
	execute: \psql tournament<br>
5. Import the tournament.sql file (Creates db and tables)
	execute: \i tournament.sql<br>
6. Stop psql utility
	hit 'ctrl + z'
7. Execute the tests from the command prompt:<br>
   execute: python tournament_test.py

Credits to Udacity & Stackoverflow
