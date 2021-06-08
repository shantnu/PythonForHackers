#!/usr/bin/python3
import sqlite3
import subprocess


def create_db():
    db = "./students.db"

    # delete the database if it exists already
    proc = subprocess.Popen(["rm " + db], shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout,stderr = proc.communicate()
    #print(stdout, stderr)

    conn = sqlite3.connect(db)
    c = conn.cursor()

    cmd = "CREATE TABLE students (Name TEXT, Age INT)"
    c.execute(cmd)
    conn.commit()

    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]

    c.executemany("INSERT INTO students VALUES (?,?)", data)

    conn.commit()

    conn.close()

    print("Created database file students.db")

if __name__ == "__main__":
    create_db()