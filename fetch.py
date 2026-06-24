import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#create user table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
email TEXT UNIQUE
)
""")

#multiple user
users = [
    ("bob", 23, "boc@gmail.com"),
    ("charlie", 20, "charlie@gmail.com"),
    ("panda", 30, "panda@gmail.com"),
    ("happy", 20, "happy@gamil.com"),
    ("alice", 90, "alice@gmail.com")
    
    ]

    #insert multiple records
cursor.executemany(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        users
    )

    #save changes
conn.commit()

    #fetch all users
cursor.execute ("SELECT *FROM users")
rows = cursor. fetchall()
     
print("users in database:")
for row in rows:
    print(row)

#connection close
conn.close()


