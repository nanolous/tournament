#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2

# Method to connect to DB.
def connect():
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print "Unable to connect to database"

def deleteMatches():
    DB = connect()
    c = DB.cursor()
    SQL = "DELETE FROM Matches"
    # Deletes all matches from matches table.
    c.execute(SQL)
    DB.commit()
    DB.close()

def deletePlayers():
    DB = connect()
    c = DB.cursor()
    SQL = "DELETE FROM Players"
    # Deletes all players from players table.
    c.execute(SQL)
    DB.commit()
    DB.close()

def countPlayers():
    DB = connect()
    c = DB.cursor()
    SQL = "SELECT COUNT(*) FROM Players"
    # Selects the count of players from the players table.
    c.execute(SQL)
    # Returns a single row.
    rows = c.fetchone()
    DB.commit()
    # Returns fetched result set from rows variable.
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
    # Define SQL query. Insert into the players table, passing in name variable from unit test method.
    SQL = "INSERT INTO Players (name) VALUES (%s);"
    # Sets data to name tuple for cursor.
    data = (name,)
    # Cursor executes SQL query, passing in the data tuple for insert.
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
    # Standings view commented in tournament_test.py.
    SQL = "SELECT * FROM Standings"
    c.execute(SQL)
    # Fetch all rows.
    rows = c.fetchall()
    DB.commit()
    return rows
    DB.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    # Insert string variables into matches table.
    SQL = "INSERT INTO Matches(winner, loser) VALUES (%s, %s);"
    # Data variable tuple for cursor.
    data = (winner, loser)
    # Execute SQL passing in the string variables.
    c.execute(SQL, data)
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
    # Swiss_pairings view commented in tournament_test.py.
    SQL = "SELECT * FROM Swiss_Pairings"
    c.execute(SQL)
    # Fetch all rows.
    rows = c.fetchall()
    DB.commit()
    return rows
    DB.close()