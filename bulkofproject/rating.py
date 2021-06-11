import sqlite3

from flask import redirect


def Game(request):
    Game = request.form['Rating2']
    Rating = request.form['Rating']
    Comments = request.form['Comments']
    print("Game" + "\t" + Game + "\t" + "Comments" + "\t" + Rating + "\t" + "Rating" + "\t" + Comments)
    userinfo = [Game, Rating, Comments]
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", userinfo)
    # Commit our command
    conn.commit()

    # close our connection
    conn.close()