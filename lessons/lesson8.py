import sqlite3

connect = sqlite3.connect("user_grades.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR (50) NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")
connect.commit()

def create_user(name, age, hobby):
    #cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
        (name, age, hobby)
    )
    connect.commit()
    print("user added!!")

# create_user("user", 16, "Спать")
# create_user("user2", 12, "Плавать")
# create_user("user3", 2, "Плавать")

def create_grade(user_id, subject, grade):
    cursor.execute(
        'INSERT INTO grades(subject, grade, user_id) VALUES (?,?,?)',
        (subject, grade, user_id)
    )
    connect.commit()
    print('grade added!!!')

# create_grade(1, "Алегра", 3)
# create_grade(2, "Химия", 4)
# create_grade(2, "Физика", 5)

def  read_users_and_grades():
    cursor.execute('''
        
        SELECT users.name, grades.subject, grades.grade
        FROM users FULL OUTER JOIN grades ON users.id = grades.user_id
        
    ''')
    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]} SUBJECT: {i[1]} GRADE: {i[2]}")

# read_users_and_grades()

# MAX() MIN() AVG() - COUNT() SUM()
def get_max_age():
    cursor.execute('SELECT SUM(age) FROM users')
    users = cursor.fetchall()
    print(users)

# get_max_age()

# VIEW - Передставление


def create_my_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS view_test AS
        SELECT name, age, subject, grade
        FROM users LEFT JOIN grades ON users.id = grades.user_id
        WHERE age = 26
    """)
    print('VIEW added')
    connect.commit()
# create_my_view()

def get_view():
    cursor.execute('SELECT * FROM view_test')
    users = cursor.fetchall()
    print(users)

# get_view()