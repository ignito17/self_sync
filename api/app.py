# self_sync_core-a2, self_sync_web-a1
# api/api.py

from flask import Flask, request, jsonify, render_template
import sqlite3
import os 
from datetime import datetime

# Creating the Flask app
app = Flask(__name__)
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'data.sqlite'))

# Creating the base route
@app.route("/")
def index():
    # return "🧠 Self Sync API is live!"
    return render_template(index.html)

# Route to acess /add_note api
@app.route("/add_note", methods=["POST"])
def add_note():
    data=request.get_json()
    title=data.get("title")
    desc=data.get("desc")
    if not title or not desc:
        return jsonify({"status": "fail", "msg": "Missing title or desc"}), 400
    try:
        conn=sqlite3.connect(DB_PATH)
        cur=conn.cursor()
        cur.execute(
            "INSERT INTO diary_entries (title, description,timestamp) VALUES (?, ?, ?)",
            (title, desc, datetime.now().isoformat())
        )
        conn.commit()
        conn.close()
        return jsonify({"status":"sucess", "msg":"Note Added"}), 201
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}), 500

# Route to access /add_pomo api
@app.route("/add_pomo",methods=["POST"])
def add_pomo():
    data=request.get_json()
    minutes=data.get("minutes")
    topic=data.get("topic")
    if not minutes or not topic:
        return jsonify({"error":"Missing Fields"}), 400
    conn=sqlite3.connect(DB_PATH)
    c=conn.cursor()
    c.execute("""
                INSERT INTO pomo_sessions (minutes,topic,timestamp)
                VALUES (?,?,?)""",
                (minutes,topic,datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({"message": f"✅ Pomo of {minutes} mins on '{topic}' logged."})

# Route to access /add_expense api
@app.route("/add_expense",methods=["POST"])
def add_expense():
    data=request.get_json(force=True)
    amount,desc=data.get("amount"),data.get("desc","").strip()
    if not amount or not desc:
        return jsonify({"error":"Missing Fields"})
    conn=sqlite3.connect(DB_PATH)
    c=conn.cursor()
    c.execute("""
                INSERT INTO expenses (amount,desc,timestamp)
                VALUES (?,?,?)""",(amount,desc,datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({"message": f"💸 Expense of ₹{amount} for '{desc}' logged."})

# Route to access /review API
@app.route("/review", methods=["POST"])
def add_review():
    data = request.get_json(force=True)
    title = data.get("title", "").strip()
    desc = data.get("desc", "").strip()

    if not title or not desc:
        return jsonify({"status": "fail", "msg": "Missing title or desc"}), 400

    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO reviews (title, description, timestamp)
            VALUES (?, ?, ?)""",
            (title, desc, datetime.now().isoformat()))
        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "msg": f"📋 Review '{title}' logged successfully."
        }), 201
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__=="__main__":
    app.run()
    # app.run(host="127.0.0.1", port=5000, debug=True)