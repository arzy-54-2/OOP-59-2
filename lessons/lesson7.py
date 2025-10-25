import sqlite3

# A4
connect = sqlite3.connect("users.db")

# Рука и Ручка
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
connect.commit()


# CRUD Create Read Update Delete

def create_user(name, age, hobby):
    #cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print("user added!!")

# create_user('Stas', 23, "Спать")



def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    # print(users)
    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]} HOBBY: {i[2]}")

# read_users()

def update_user(new_name, rowid):
    # cursor.execute(f'UPDATE users SET name = "{new_name}" WHERE rowid = "{rowid}"')
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (new_name, rowid)
    )
    connect.commit()
    print("user updated!!")

update_user("Nikita", 3)

# read_users()

def delete_user(rowid):
    cursor.execute(f"DELETE FROM users WHERE rowid = '{rowid}'")
    connect.commit()
    print('Users deleted!!')

# delete_user(2)