from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('visitors.db')
    cursor = conn.cursor()

    # Increase visit count
    cursor.execute("UPDATE counter SET visits = visits + 1 WHERE id = 1")
    conn.commit()

    # Fetch updated value
    cursor.execute("SELECT visits FROM counter WHERE id = 1")
    visits = cursor.fetchone()[0]

    conn.close()

    return render_template("index.html", visits=visits)

if __name__ == "__main__":
    app.run(debug=True)