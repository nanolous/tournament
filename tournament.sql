-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE PLAYERS (
ID SERIAL PRIMARY KEY,
Name TEXT);

CREATE TABLE MATCHES (
ID SERIAL,
Winner INTEGER references PLAYERS(ID),
Loser INTEGER references PLAYERS(ID));

CREATE TABLE PLAYER_STANDINGS (
ID SERIAL,
Player1 INTEGER,
Player2 INTEGER);

CREATE VIEW AS STANDINGS 
SELECT players.id, players.name,COUNT(matches.winner) AS wins, 
COUNT(DISTINCT matches.loser) + COUNT(matches.winner) AS matches 
FROM players LEFT JOIN matches ON players.id = matches.winner 
GROUP BY players.id ORDER BY wins DESC;

