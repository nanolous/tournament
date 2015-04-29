<b>Udacity Database Project<b>

This project is a tournament game engine.

It effectively exercies SQL to create the DB structure, players, matches, and more.

Postgresql and Psycopg2 are the tools for development.

Setup:
========
1. Download the tournament zip file<br>
2. Extract the zip file to a directory<br>
3. Launch a command prompt<br>
4. Navigate to the zip file directory<br>
5. Launch psql utility<br>
	execute: psql tournament<br>
6. Create the Database<br>
	a. Either import the tournament.sql db file or execute: CREATE DATABASE tournament;<br>
	b. Import the tournament.sql file. Creates the database, connects to the database and creates the tables.<br>
	execute: \i tournament.sql<br>
7. Stop psql utility<br>
	hit 'ctrl + z'<br>
8. Navigate to the directory containing the tournament_test.py file
9. Execute the tests from the command prompt:<br>
   	execute: python tournament_test.py<br>

Credits to Udacity & Stackoverflow