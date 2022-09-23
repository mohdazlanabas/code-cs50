from cs50 import SQL
import csv

db = SQL("sqlite:///favorites.db")
title = input("title: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", title)

row = rows[0]

print(row["counter"])
