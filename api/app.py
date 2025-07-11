# self_sync_core-a2, self_sync_web-a1
# api/api.py

from flask import Flask, request, jsonify
import sqlite3
import os 
from datetime import datetime

# Creating the Flask app
app = Flask(__name__)
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'data.sqlite'))

@app.route("/")
def index():
    return "🧠 Self Sync API is live!"

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

if __name__=="__main__":
    app.run()
    # app.run(host="127.0.0.1", port=5000, debug=True)