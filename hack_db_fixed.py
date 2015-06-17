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

Name_to_use = (Name,)
print("Name to use:", Name_to_use)
c.execute("SELECT * from students WHERE Name=(?)" , Name_to_use)

result = c.fetchall()
print result

