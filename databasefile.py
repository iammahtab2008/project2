import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT,
            lname TEXT,
            course TEXT,
            password TEXT)
                           ''')
        self.connection.commit()

    def insert(self, fname, lname, course, password):
        self.cursor.execute("INSERT INTO users (fname, lname, course, password) VALUES (?, ?, ?, ?)",
                            (fname, lname, course, password))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id))
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def find_user_by_password(self, password):
        self.cursor.execute("SELECT fname, lname FROM users WHERE password = ?", (password,))
        return self.cursor.fetchone()
    
    def get_all_passwords(self):
        self.cursor.execute("SELECT password FROM users")
        return self.cursor.fetchall()
