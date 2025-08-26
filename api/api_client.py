# 📁 self_sync/modules/api_client.py
# Client for the api host, i.e. could be used to connect and bridge data out and in.

import requests
import os

# Use env var or fallback to localhost
BASE_URL = os.getenv("SELF_SYNC_API", "http://127.0.0.1:5000")

# Client side api call to api host
def add_note(title:str,content:str):
    data={"title":title,"content":content}
    try:
        r=requests.post(f"{BASE_URL}/add_note",json=data)
        return r.json()
    except Exception as e:
        return {"error":str(e)}
    

def add_pomo(label:str,duration:int):
    data={"label":label,"duration":duration}
    try:
        r=requests.post(f"{BASE_URL}/add_pomo", json=data)
        return r.json()
    except Exception as e:
        return {"error":str(e)}
    

def add_expense(amount:int,description:str):
    data={"amount":amount,"desc":description}
    try:
        r=requests.post(f"{BASE_URL}/add_expense",json=data)
        return r.json()
    except Exception as e:
        return {"error":str(e)}

def get_review():
    try:
        r = requests.get(f"{BASE_URL}/review")
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def view_notes():
    try:
        r = requests.get(f"{BASE_URL}/view_notes")
        return r.json()
    except Exception as e:
        return {"error": str(e)}