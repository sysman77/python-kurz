import sqlite3

def setup_database():
    # Připojení k databázi (vytvoří novou databázi, pokud neexistuje)
    conn = sqlite3.connect('chat_app.db')
    cursor = conn.cursor()

    # Vytvoření tabulky uživatelů
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    # Vložení uživatelů
    cursor.executemany('''
    INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
    ''', [('user1', 'password1'), ('user2', 'password2'), ('user3', 'password3')])

    # Vytvoření tabulky místností
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')

    # Vložení místností
    cursor.executemany('''
    INSERT OR IGNORE INTO rooms (name) VALUES (?)
    ''', [('Room 1',), ('Room 2',), ('Room 3',)])

    # Vytvoření tabulky zpráv
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        room_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (room_id) REFERENCES rooms(id)
    )
    ''')

    # Uložení změn a uzavření spojení s databází
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete. chat_app.db has been created and populated.")
