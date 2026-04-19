import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name TEXT,
                age INTEGER
            )
        """)
        self.conn.commit()

    def add_user(self, name, age):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_age(self, name, new_age):
        self.cursor.execute("UPDATE users SET age = ? WHERE name = ?", (new_age, name))
        self.conn.commit()

    def delete_user(self, name):
        self.cursor.execute("DELETE FROM users WHERE name = ?", (name,))
        self.conn.commit()

    def close(self):
        self.conn.close()
```

Kodni ishlatish uchun misol:
```python
db = Database("users.db")
db.add_user("John", 25)
db.add_user("Alice", 30)

print(db.get_all())  # [(John, 25), (Alice, 30)]

db.update_age("John", 26)
print(db.get_all())  # [(John, 26), (Alice, 30)]

db.delete_user("Alice")
print(db.get_all())  # [(John, 26)]

db.close()
