#!/usr/bin/python3
import sqlite3

def hack_db_fixed():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()

    print("Without Hack: \n")

    c.execute("SELECT * from students WHERE Name='Robert'")
    result = c.fetchall()
    print(result)

    print("With Hack: \n")
    Name = "Robert'; DROP TABLE students;--"

    Name_to_use = (Name,)
    print("Name to use:", Name_to_use)
    c.execute("SELECT * from students WHERE Name=(?)" , Name_to_use)

    result = c.fetchall()
    print(result)

    data = [("Robert'; DROP TABLE students;--", 10)]
    c.executemany("INSERT INTO students VALUES (?,?)", data)
    conn.commit()

    Name_to_use = (Name,)
    print("Name to use:", Name_to_use)
    c.execute("SELECT * from students WHERE Name=(?)" , Name_to_use)

    result = c.fetchall()
    print(result)

    conn.close()

    return result

if __name__ == "__main__":
    hack_db_fixed()
