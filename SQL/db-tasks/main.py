import sqlite3
from datetime import datetime, timedelta

# Připojení k databázi
conn = sqlite3.connect('chat_app.db')
cursor = conn.cursor()

# 1. Získá všechny messages a jména jejich autorů z databáze chat_app.db
def get_all_messages_with_authors():
    query = '''
    SELECT messages.message, users.username
    FROM messages
    JOIN users ON messages.user_id = users.id
    '''
    cursor.execute(query)
    return cursor.fetchall()

# 2. Získá seznam všech rooms a posledních 5 messages z nich
def get_last_five_messages_per_room():
    query = '''
    SELECT rooms.name, messages.message
    FROM rooms
    JOIN messages ON rooms.id = messages.room_id
    WHERE messages.id IN (
        SELECT id FROM messages AS m
        WHERE m.room_id = rooms.id
        ORDER BY m.timestamp DESC
        LIMIT 5
    )
    ORDER BY rooms.name, messages.timestamp DESC
    '''
    cursor.execute(query)
    return cursor.fetchall()

# 3. Získá všechny messages za posledních 24 hodin a jména jejich username
def get_messages_last_24_hours():
    last_24_hours = datetime.now() - timedelta(days=1)
    # Převod datetime na řetězec ve formátu ISO (který SQLite rozumí)
    last_24_hours_str = last_24_hours.strftime('%Y-%m-%d %H:%M:%S')

    query = '''
    SELECT messages.message, users.username
    FROM messages
    JOIN users ON messages.user_id = users.id
    WHERE messages.timestamp >= ?
    '''
    cursor.execute(query, (last_24_hours_str,))
    return cursor.fetchall()

# 4. Získá seznam username a počet messages které každý napsal
def get_message_count_per_user():
    query = '''
    SELECT users.username, COUNT(messages.id) AS message_count
    FROM users
    JOIN messages ON users.id = messages.user_id
    GROUP BY users.username
    ORDER BY message_count DESC
    '''
    cursor.execute(query)
    return cursor.fetchall()

# 5. Získá seznam rooms a počet zpráv v každé z nich
def get_message_count_per_room():
    query = '''
    SELECT rooms.name, COUNT(messages.id) AS message_count
    FROM rooms
    JOIN messages ON rooms.id = messages.room_id
    GROUP BY rooms.name
    ORDER BY message_count DESC
    '''
    cursor.execute(query)
    return cursor.fetchall()

# 6. Získá seznam username a jejich celkový počet messages v každé rooms
def get_user_message_count_per_room():
    query = '''
    SELECT users.username, rooms.name, COUNT(messages.id) AS message_count
    FROM users
    JOIN messages ON users.id = messages.user_id
    JOIN rooms ON rooms.id = messages.room_id
    GROUP BY users.username, rooms.name
    ORDER BY users.username, rooms.name
    '''
    cursor.execute(query)
    return cursor.fetchall()

# Výpis výsledků
print("1. Všechny zprávy a jména jejich autorů:")
print(get_all_messages_with_authors())

print("\n2. Seznam všech místností a posledních 5 zpráv z nich:")
print(get_last_five_messages_per_room())

print("\n3. Všechny zprávy za posledních 24 hodin a jména jejich autorů:")
print(get_messages_last_24_hours())

print("\n4. Seznam uživatelů a počet zpráv, které každý napsal:")
print(get_message_count_per_user())

print("\n5. Seznam místoností a počet zpráv v každé z nich:")
print(get_message_count_per_room())

print("\n6. Seznam uživatelů a jejich celkový počet zpráv v každé rooms:")
print(get_user_message_count_per_room())

# Uzavření spojení s databází
conn.close()
