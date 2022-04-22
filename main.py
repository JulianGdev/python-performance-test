import psycopg2 as psycopg2
from fastapi import FastAPI


app = FastAPI(title="Python Performance Test")


@app.get("/api/users")
def get_users():
    return get_users_db()


def get_users_db():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = []
    for id, name, *others in cur.fetchall():
        users.append({"id": id, "name": name})
    return users


def db_connect():
    return psycopg2.connect(
        dbname="test",
        user="juliang",
        password="localpass",
        host="localhost",
        port="5432",
    )
