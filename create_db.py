import sqlite3

#  Create a new database file
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

#  Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Create Transactions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    status TEXT CHECK(status IN ('Pending', 'Completed', 'Failed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

#  Insert Sample Data
users_data = [
    ("Alice Johnson", "alice@example.com"),
    ("Bob Smith", "bob@example.com"),
    ("Charlie Brown", "charlie@example.com")
]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users_data)

transactions_data = [
    (1, 250.00, "Completed"),
    (2, 75.50, "Pending"),
    (3, 320.00, "Failed"),
    (1, 150.00, "Completed"),
    (2, 500.00, "Completed")
]
cursor.executemany("INSERT INTO transactions (user_id, amount, status) VALUES (?, ?, ?)", transactions_data)

#  Save changes and close
conn.commit()
conn.close()

print("✅ New data.db created successfully!")
