-- Creates the Tournament db.
CREATE DATABASE Tournament;

-- Create Players table if it doesn't exist.
CREATE TABLE IF NOT EXISTS Players (
-- ID column is the primary key.
ID SERIAL PRIMARY KEY,
-- Name column 'Text' data type.
Name TEXT);

-- Create Matches table if it doesn't exist.
CREATE TABLE IF NOT EXISTS Matches (
-- Generates unique id per match.
ID SERIAL,
-- Winner column references the ID primary key from the players table.
Winner INTEGER references PLAYERS(ID),
-- Loser column references the ID primary key from the players table.
Loser INTEGER references PLAYERS(ID));

-- Create Standings view.
CREATE VIEW Standings AS
-- Define the columns (players id, and players name) from players table.
SELECT p.id, p.name, 
-- Define column (alias) wins from aliased matches (m1) table.
(SELECT COUNT(m1.winner)) AS Wins,
-- Define column (alias) Matches, aggregating total of wins and matches for loser/winner.
	-- Aliased (m2) for winner table to exclude m1 wins, avoiding duplicate count for winner.
(SELECT COUNT(m2.loser) + COUNT(m1.winner)) AS Matches
-- Aliased table Players(p) referenced in FROM clause. 
	-- Executes a JOIN on m1 to match player id with matches winner id.
FROM Players p LEFT OUTER JOIN Matches m1 ON p.id = m1.winner
-- Exexcutes a JOIN on m2 to match player id with matches loser id.
LEFT OUTER JOIN Matches m2 ON p.id = m2.loser
-- GROUP BY clause by player id and ORDER BY wins.
GROUP BY p.id ORDER BY wins DESC;

-- Create Swiss_Pairings view.
CREATE VIEW Swiss_Pairings AS
-- Define columns as ID1, Name1, ID2, Name2 from players table, exluding duplicates (DISTINCT).
SELECT DISTINCT p1.ID AS ID1, 
p1.Name AS Name1, p2.ID AS ID2, p2.Name AS Name2 
-- Select FROM aliased Standings p1, and Standings p2 tables for matching in the WHERE clause.
FROM Standings p1, Standings p2
-- WHERE clause matches from aliased tables only matching if player id contains same win record.
	-- p1.id<>p2.id ensures only unique players returned in result set, indicating p1.id cannot equal p2.id.
	-- LIMIT clause ensures only two rows are returned.
WHERE p1.wins = p2.wins AND p1.id <> p2.id LIMIT 2;