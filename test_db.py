from create_db import create_db
from hack_db import hack_db
from hack_db_fixed import hack_db_fixed

def test_hackdb():
    create_db()
    result = hack_db()
    assert result == []

def test_hack_db_fixed():
    create_db()
    result = hack_db_fixed()
    assert result == [("Robert'; DROP TABLE students;--", 10)]