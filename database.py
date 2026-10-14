import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_student(name, score):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

def get_student(name_query):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM students WHERE name LIKE ?", ('%' + name_query + '%',))
    data = cursor.fetchall()
    conn.close()
    return data

init_db()