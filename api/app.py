# -*- coding: utf-8 -*-
# self_sync_core-a2, self_sync_web-a1
# api/api.py
# web api hoster with route and data definitions

import os 
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from modules import diary_logger, money_tracker, stats_viewer, time_tracker

BASE_DIR = os.path.dirname(__file__)

# Creating the Flask app
app = Flask("Self Sync",
            template_folder=os.path.join(BASE_DIR, "templates")
            )
# DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'data.sqlite'))

# Creating the base route
@app.route("/")
def index():
    # return "🧠 Self Sync API is live!"
    return render_template("index.html")

# Route to acess /add_note api
@app.route("/add_note", methods=["POST"])
def add_note():
    data=request.get_json()
    title=data.get("title")
    desc=data.get("desc")
    if not title or not desc:
        return jsonify({"status": "fail", "msg": "Missing title or desc"}), 400
    try:
        # conn=sqlite3.connect(DB_PATH)
        # cur=conn.cursor()
        # cur.execute(
        #     "INSERT INTO diary_entries (title, description,timestamp) VALUES (?, ?, ?)",
        #     (title, desc, datetime.now().isoformat())
        # )
        # conn.commit()
        # conn.close()
        diary_logger.add_note(title=title,desc=desc)
        
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
    time_tracker.add_pomo(minutes=minutes,topic=topic)
    
    return jsonify({"message": f"✅ Pomo of {minutes} mins on '{topic}' logged."}), 201

# Route to access /add_expense api
@app.route("/add_expense",methods=["POST"])
def add_expense():
    data=request.get_json(force=True)
    amount,desc=data.get("amount"),data.get("desc","").strip()
    if not amount or not desc:
        return jsonify({"error":"Missing Fields"}), 400
    money_tracker.add_expense(amount=amount,description=desc)
    
    return jsonify({"message": f"💸 Expense of ₹{amount} for '{desc}' logged."}), 201

# Route to access /review API
@app.route("/review", methods=["GET","POST"])
def get_review():
    data = request.get_json(force=True)
    title = data.get("title", "").strip()
    desc = data.get("desc", "").strip()

    if not title or not desc:
        return jsonify({"status": "fail", "msg": "Missing title or desc"}), 400

    try:
        return jsonify({
            "status": "success",
            "msg": f"📋 Review '{title}' fetched successfully.",
            "review": stats_viewer.send_review()
        }), 201
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__=="__main__":
    app.run()
    # app.run(host="127.0.0.1", port=5000, debug=True)