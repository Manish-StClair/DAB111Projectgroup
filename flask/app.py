from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    # Provide data source and variable definitions
    return render_template('about.html')

@app.route('/data')
def display_data():
    # Fetch a sample of data from the SQLite database
    con = sqlite3.connect('python_project.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Canada_employment ORDER BY RANDOM() LIMIT 10")  # Fetch 10 random rows
    sample_data = cursor.fetchall()
    con.close()
    return render_template('data.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)
