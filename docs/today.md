# 📆 2025-07-11 – Self Sync Phase 2, Day 1

### 🔧 Focus
Flask API Bootstrapping – `/add_note` endpoint

### ⏱️ Time Budget
3 hours total

### ✅ What I Did
- Created `api/` folder and Flask app
- Connected Flask to `db/data.sqlite`
- Built `/add_note` route using JSON POST
- Successfully tested with Postman
- Validated note was inserted in DB

### 📎 Notes
- Used `os.path` to dynamically resolve DB path
- Reused schema from `diary_logger.py` to avoid duplication

### 📍 Next Step
- Add `/view_notes` route
- Export notes to CSV
