from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "events.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            venue TEXT NOT NULL,
            organizer TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            email TEXT NOT NULL,
            branch TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events(id)
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db()
    events = conn.execute(
        "SELECT * FROM events ORDER BY date"
    ).fetchall()
    conn.close()

    return render_template("index.html", events=events)


@app.route("/events")
def events():
    conn = get_db()

    events = conn.execute(
        "SELECT * FROM events ORDER BY date"
    ).fetchall()

    conn.close()

    return render_template("events.html", events=events)


@app.route("/add-event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        date = request.form["date"]
        venue = request.form["venue"]
        organizer = request.form["organizer"]

        conn = get_db()

        conn.execute("""
            INSERT INTO events
            (name, description, date, venue, organizer)
            VALUES (?, ?, ?, ?, ?)
        """, (
            name,
            description,
            date,
            venue,
            organizer
        ))

        conn.commit()
        conn.close()

        return redirect(url_for("events"))

    return render_template("add_event.html")


@app.route("/register/<int:event_id>", methods=["POST"])
def register(event_id):
    student_name = request.form["student_name"]
    email = request.form["email"]
    branch = request.form["branch"]

    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    if event:
        conn.execute("""
            INSERT INTO registrations
            (event_id, student_name, email, branch)
            VALUES (?, ?, ?, ?)
        """, (
            event_id,
            student_name,
            email,
            branch
        ))

        conn.commit()

    conn.close()

    return redirect(url_for("events"))


@app.route("/registrations/<int:event_id>")
def registrations(event_id):
    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    registrations = conn.execute("""
        SELECT * FROM registrations
        WHERE event_id = ?
    """, (event_id,)).fetchall()

    conn.close()

    return render_template(
        "registrations.html",
        event=event,
        registrations=registrations
    )


@app.route("/delete-event/<int:event_id>", methods=["POST"])
def delete_event(event_id):
    conn = get_db()

    conn.execute(
        "DELETE FROM registrations WHERE event_id = ?",
        (event_id,)
    )

    conn.execute(
        "DELETE FROM events WHERE id = ?",
        (event_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("events"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)