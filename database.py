import sqlite3

DB_NAME = "channels.db"

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

# ==========================
# CREATE TABLE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS channels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE
)
""")

conn.commit()


# ==========================
# ADD CHANNEL
# ==========================

def add_channel(username):
    try:
        cursor.execute(
            "INSERT INTO channels (username) VALUES (?)",
            (username,)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False


# ==========================
# REMOVE CHANNEL
# ==========================

def remove_channel(username):
    cursor.execute(
        "DELETE FROM channels WHERE username=?",
        (username,)
    )
    conn.commit()


# ==========================
# GET ALL CHANNELS
# ==========================

def get_channels():
    cursor.execute(
        "SELECT username FROM channels"
    )

    rows = cursor.fetchall()

    return [row[0] for row in rows]


# ==========================
# CHECK CHANNEL EXISTS
# ==========================

def channel_exists(username):
    cursor.execute(
        "SELECT 1 FROM channels WHERE username=?",
        (username,)
    )

    return cursor.fetchone() is not None


# ==========================
# CLEAR ALL CHANNELS
# ==========================

def clear_channels():
    cursor.execute(
        "DELETE FROM channels"
    )
    conn.commit()


# ==========================
# TOTAL CHANNELS
# ==========================

def get_channel_count():
    cursor.execute(
        "SELECT COUNT(*) FROM channels"
    )

    return cursor.fetchone()[0]


# ==========================
# CLOSE DATABASE
# ==========================

def close_database():
    conn.close()
