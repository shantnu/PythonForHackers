
# coding: utf-8

# In[87]:

import sqlite3


# In[94]:

db = "./students.db"
conn = sqlite3.connect(db)
c = conn.cursor()


# In[69]:

#c.execute("DROP table students")


# In[95]:

cmd = "CREATE TABLE students (Name TEXT,                               Age INT)"

c.execute(cmd)


# In[96]:

conn.commit()


# In[97]:

conn.close()


# In[99]:

db = "./students.db"
conn = sqlite3.connect(db)
c = conn.cursor()


# In[86]:

c.execute("SELECT * from students")
result = c.fetchall()
print result


# In[81]:

c.execute("SELECT * from students WHERE Name='James'")
result = c.fetchall()
print result


# In[100]:

Name = "James'; DROP TABLE students;--"
print "SELECT * from students WHERE Name='%s'" % Name
c.executescript("SELECT * from students WHERE Name='%s'" % Name)
#c.executescript("SELECT * from students WHERE Name = 'James'; DROP TABLE students;")
result = c.fetchall()
print result


# In[84]:

conn.close()


# In[ ]:



