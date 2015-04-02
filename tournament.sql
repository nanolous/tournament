-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- PLayers table, where the primary key is defined, and name field.
CREATE TABLE PLAYERS (
ID SERIAL PRIMARY KEY,
Name TEXT);

-- Matches table, unique serial ID, and winner/loser columns that reference the primary key in players table.
CREATE TABLE MATCHES (
ID SERIAL,
Winner INTEGER references PLAYERS(ID),
Loser INTEGER references PLAYERS(ID));

-- Standings view, aggregates matches data per player with fields specified from players table, and a join from the matches table.
CREATE VIEW STANDINGS AS
SELECT players.id, players.name,COUNT(matches.winner) AS wins, 
COUNT(DISTINCT matches.loser) + COUNT(matches.winner) AS matches 
FROM players LEFT JOIN matches ON players.id = matches.winner 
GROUP BY players.id ORDER BY wins DESC;