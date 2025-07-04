from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('chama.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            amount_due REAL DEFAULT 0,
            amount_paid REAL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('chama.db')
    c = conn.cursor()
    c.execute('SELECT * FROM members')
    members = c.fetchall()
    conn.close()
    return render_template('index.html', members=members)

@app.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        amount_due = request.form['amount_due']
        
        conn = sqlite3.connect('chama.db')
        c = conn.cursor()
        c.execute('INSERT INTO members (name, phone, amount_due) VALUES (?, ?, ?)',
                  (name, phone, amount_due))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_member.html')

@app.route('/pay/<int:member_id>', methods=['POST'])
def pay(member_id):
    amount = float(request.form['amount'])
    conn = sqlite3.connect('chama.db')
    c = conn.cursor()
    c.execute('UPDATE members SET amount_paid = amount_paid + ? WHERE id = ?', (amount, member_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/send_reminders')
def send_reminders():
    conn = sqlite3.connect('chama.db')
    c = conn.cursor()
    c.execute('SELECT name, phone, amount_due, amount_paid FROM members')
    members = c.fetchall()
    conn.close()

    reminders = []
    for member in members:
        name, phone, due, paid = member
        if paid < due:
            msg = f"Reminder sent to {name} ({phone}): Please pay balance of KES {due - paid}."
            print(msg)  # This will print in your terminal
            reminders.append(msg)
    
    return "<br>".join(reminders) or "All members have paid in full!"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
