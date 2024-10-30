from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        search = request.form['search']
        results = conn.execute('SELECT * FROM items WHERE name LIKE ?', ('%' + search + '%',)).fetchall()
    else:
        results = []
    conn.close()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
