#!/usr/bin/python3
import sqlite3
from subprocess import *

db = "./students.db"

# delete the database if it exists already
proc = Popen(["rm " + db], shell = True,stdin=PIPE,stdout=PIPE,stderr=PIPE)

stdout,stderr = proc.communicate()  
print(stdout, stderr)

conn = sqlite3.connect(db)
c = conn.cursor()

cmd = "CREATE TABLE students (Name TEXT, Age INT)"
c.execute(cmd)
conn.commit()

data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]

c.executemany("INSERT INTO students VALUES (?,?)", data)

conn.commit()

conn.close()
