import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "guestbook"),
        user=os.getenv("DB_USER", "guestbook"),
        password=os.getenv("DB_PASSWORD", "guestbook")
    )


def initialize_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


@app.route("/")
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, name, message, created_at
        FROM messages
        ORDER BY created_at DESC
    """)

    messages = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", messages=messages)


@app.route("/add", methods=["POST"])
def add_message():
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not message:
        return redirect(url_for("index"))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages (name, message)
        VALUES (%s, %s)
        """,
        (name, message)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    initialize_database()

    app.run(
        host="0.0.0.0",
        port=5000
    )
