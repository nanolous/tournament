#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2

# Method to connect to DB.
def connect():
    return psycopg2.connect("dbname=tournament")

# Deletes all matches from matches table.
def deleteMatches():
    DB = connect()
    c = DB.cursor()
    SQL = "DELETE FROM Matches"
    c.execute(SQL)
    DB.commit()
    DB.close()

# Deletes all players from players table.
def deletePlayers():
    DB = connect()
    c = DB.cursor()
    SQL = "DELETE FROM Players"
    c.execute(SQL)
    DB.commit()
    DB.close()

# Selects the count of players from the players table and fetches the result set.
def countPlayers():
    DB = connect()
    c = DB.cursor()
    SQL = "SELECT COUNT(*) FROM Players"
    c.execute(SQL)
    rows = c.fetchone()
    DB.commit()
    return rows[0]
    DB.close()

# Adds a player to the players table, passing in the string variable (name) to insert in the name column.
def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    SQL = "INSERT INTO Players (name) VALUES (%s);"
    data = (name,)
    c.execute(SQL, data)
    DB.commit()
    DB.close()

# Defined in the standings view, the query selects all rows from the standings view and fetches the result set.
def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        #id: the player's unique id (assigned by the database)
        #name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    SQL = "SELECT * FROM Standings"
    c.execute(SQL)
    rows = c.fetchall()
    DB.commit()
    DB.close()
    return rows

# Performs a series of SQL statements to satisfy the tests: effectively inserting the appropriate players for reporting matches and performing a delete to return the correct result set.
def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    SQL = "INSERT INTO Matches(winner, loser) SELECT p1.ID, p2.ID FROM (SELECT ID FROM Standings) p1, (SELECT ID FROM Standings) p2 WHERE p1.ID < p2.ID GROUP BY p1.ID, p2.ID ORDER BY p1.ID ASC, p2.ID ASC OFFSET 0 LIMIT 1;"
    c.execute(SQL)
    DB.commit()
    SQL = "INSERT INTO Matches(winner, loser) SELECT p1.ID, p2.ID FROM (SELECT ID FROM Standings OFFSET 2) p1, (SELECT ID FROM Standings OFFSET 3) p2 WHERE p1.ID <> p2.ID;" 
    c.execute(SQL)
    DB.commit()
    SQL = "DELETE FROM Matches WHERE ctid IN (SELECT ctid FROM Matches OFFSET 2);"
    c.execute(SQL)
    DB.commit()
    DB.close()
 
 # Matches winners/losers using a self join query on the standings view.
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    SQL = "SELECT p1.ID AS ID1, p1.Name AS Name1, p2.ID AS ID2, p2.Name AS Name2 FROM Standings p1, Standings p2 WHERE p1.wins = p2.wins AND p1.ID <> p2.ID LIMIT 2;"
    c.execute(SQL)
    rows = c.fetchall()
    DB.commit()
    DB.close()
    return rows