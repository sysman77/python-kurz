import sqlite3


def db_insert(db_cur, table, cols, vals):
    if len(cols) != len(vals):
        return False

    columns = ",".join(cols)

    values = "?," * len(vals)

    try:
        query = f"INSERT INTO {table} ({columns}) VALUES ({values[:-1]})"
        db_cur.execute(query, vals)

    except:
        return False

    return True




connection = sqlite3.connect("my_db.db")
cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER)""")

#cursor.execute("""INSERT INTO users (name, age) VALUES ("Jan", 33)""")
#cursor.execute("""INSERT INTO users (name, age) VALUES ("Adam", 35)""")


#if not db_insert(cursor, "users", ["name", "age"], ["TEST", 99]):
#    print("došlo k chybe")

#if not db_insert(cursor, "users", ["name"], ["TEST2"]):
#    print("došlo k chybe")

connection.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

print("--------------------")
for row in rows:
    print(f"id: {row[0]} name: {row[1]}, age: {row[2]}")


connection.close()

