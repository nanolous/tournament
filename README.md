<b>Udacity Database Project<b>

This project is a tournament game engine.

It effectively exercies SQL to create the DB structure, players, matches, and more.

Postgresql and Psycopg2 are the tools for development.

Setup:<br>
=======
0. Download the tournament zip file<br>
1. Extract the zip file to a directory<br>
2. Launch a command prompt<br>
3. Navigate to the zip file directory<br>
4. Launch psql utility<br>
	execute: \psql tournament<br>
5. Import the tournament.sql file (Creates db and tables)<br>
	execute: \i tournament.sql<br>
6. Stop psql utility<br>
	hit 'ctrl + z'<br>
7. Execute the tests from the command prompt:<br>
   execute: python tournament_test.py<br>

Credits to Udacity & Stackoverflow
>>>>>>> a415cad888b2cc4eb6757349114c98e1dcc14e6c