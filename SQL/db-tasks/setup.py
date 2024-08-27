import sqlite3


conn = sqlite3.connect("chat_app.db")

cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
""")

cur.execute("""
INSERT INTO users (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3');
""")

cur.execute("""
INSERT INTO rooms (name) VALUES
('room1'),
('room2'),
('room3');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(1, 1, 'Ahoj, ako sa máte?'),
(1, 1, 'Dobre ráno všetkým!');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(1, 2, 'Dobré popoludnie!');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(2, 3, 'Ahojte, čo sa deje?');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(2, 1, 'Som tu!');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(2, 2, 'Ahoj, ako sa máte?');
""")

cur.execute("""
INSERT INTO messages (room_id, user_id, message) VALUES
(3, 3, 'Tento chat je skvelý!');
""")
conn.commit()

#cur.execute("SELECT * FROM messages")
#data = cur.fetchall()
#print(data)
conn.close()