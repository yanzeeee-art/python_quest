import sqlite3

def delete_user(user_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()

delete_user(1)