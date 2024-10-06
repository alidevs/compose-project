import os

import psycopg2
from flask import Flask

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT version()")
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Database connected: {db_version}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
