import sqlite3
def update_user(user_id, name, age, email):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
        UPDATE users
        SET name = ?, age = ?, email = ?
        WHERE id = ?
    """, (name, age, email, user_id))

    conn.commit()
    conn.close()

    #update user
update_user(2, "amyy", 26, "amy@gmail.com")
