import sqlite3 as db
base = db.connect("C:\\Users\\gk\\Documents\\myPython\\Day4\\world.db")

r = "SELECT * FROM country WHERE population>200000"
