import sqlite3
from flask import Flask, render_template, request, redirect, url_for


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
        result = conn.execute('''SELECT * FROM expenses''').fetchall()
    conn.close()
    return result()

def get_expense(expense_id):
    conn = create_connection()
    with conn:
        result = conn.execute('''select * from EXPENSES''', (expense_id)).fetchone()
    conn.close()
    return result
    

def delete_expense(expense_id): 
    conn = create_connection()
    with conn: 
        conn.execute('''DELETE FROM expenses where expense_id = ? ''', (expense_id))
    conn.close()
    
            

def update_expense(expense_id, date, category, amount, description):
    conn = create_connection()
    with conn: 
        conn.execute('''UPDATE expenses SET date = ?, category = ?, amount = ?, description = ? WHERE expense_id = ?''', (date, category, amount, description, expense_id))
    conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    expenses = get_expenses()
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 

