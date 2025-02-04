import sqlite3

DATABASE = 'financial_tracker.db'

def create_connection(): 
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(): 
    conn = create_connection()
    with conn: 
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        conn.close()

def add_expense(date, category, amount, description):
    conn = create_connection()
    with conn: 
        conn.execute('''
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        ''', (date, category, amount, description))
        conn.close()

def get_expenses(): 
    conn = create_connection()
    with conn:
        return conn.execute('''SELECT * FROM expenses''').fetchall()
    conn.close()

def get_expense(id):
    conn = create_connection()
    with conn:
        return conn.execute('''select * from EXPENSES''').fetchall()
    conn.close()

    def delete_expense(id): 
        conn = create_connection()
        with conn: 
            conn.execute('''DELETE FROM expenses where id = ? ''', (id))
            conn.close()

def update_expense(id, date, category, amount, description):
    conn = create_connection()
    with conn: 
        conn.execute('''UPDATE expenses SET date = ?, category = ?, date = ?, description = ? WHERE id = ?''', (date, category, amount, description, id))
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 