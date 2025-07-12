# 📅 Daily Logs and work tracker

---

## 🔁 Daily Update Logic (auto/manual)

> This logic defines how `today.md` will evolve daily:

- At **day start** (e.g., `2025-07-13`):
  - 🟡 Check `📍 Next Step` in yesterday’s section
  - ✏️ Append pending tasks from `📍 Next Step` to today’s "Focus" or "What I Plan"
  - 📁 Save current `today.md` as `docs/logs/2025-07-12.md` or archive folder
  - 🆕 Create fresh `today.md` for new date with carried tasks + time budget
  - 🔄 Update `perf_tracker.md` with execution block for day

---

## 📆 2025-07-11 – Self Sync Phase 2, Day 1

### 🔧 Focus [2025-07-11]

Flask API Bootstrapping – `/add_note` endpoint

### ⏱️ Time Budget [2025-07-11]

3 hours total

### ✅ What I Did [2025-07-11]

- Created `api/` folder and Flask app
- Connected Flask to `db/data.sqlite`
- Built `/add_note` route using JSON POST
- Successfully tested with Postman
- Validated note was inserted in DB

### 📎 Notes [2025-07-11]

- Used `os.path` to dynamically resolve DB path
- Reused schema from `diary_logger.py` to avoid duplication

### 📍 Next Step [2025-07-11]

- Add `/view_notes` route
- Export notes to CSV

---

### ✅ 2025-07-11

- **Start:** 12:43 PM IST
- **End:** 4:20 PM IST
- **Duration:** 3h 37m
- **Pomodoros:** 1
- **Dev Modes:** CLI, API
- **Focus Score:** 8.3 / 10
- **Tasks Completed:**
  - ✅ Added API: add_note (Flask local)
  - ✅ Triggered test via curl
  - ✅ Used main.py CLI to log pomo
  - ✅ Organized `docs/`, moved today.md and tracker
  - ✅ Committed & pushed to GitHub
- **Comments:** Strong structured session. Good file hygiene, minimal idle time.

### ✅ 2025-07-11 (Evening Session)

- **Start:** 8:25 PM IST  
- **End:** 9:50 PM IST  
- **Duration:** 1h 25m  
- **Pomodoros:** 1  
- **Dev Modes:** API Testing, HTTPie, Flask  
- **Focus Score:** 8.7 / 10  
- **Tasks Completed:**
  - ✅ Installed & configured HTTPie CLI
  - ✅ Tested `/add_pomo` and `/add_expense` endpoints
  - ✅ Fixed validation bug in `add_expense`
  - ✅ Successfully logged realistic data via CLI (compact, samosa logs 😉)
  - ✅ Git committed and pushed all updates to GitHub  
- **Comments:** Very efficient block. API interaction is smooth now. Self Sync is 75% GUI-ready.

---

## 📆 2025-07-12 – Self Sync Phase 2, Day 2

### 🔧 Focus [2025-07-12]

API Full-Cycle Testing via Termux + Validation Debug

### ⏱️ Time Budget [2025-07-12]

~1.5 hours

### ✅ What I Did [2025-07-12]

- Started Flask server from Termux
- Used HTTPie to:
  - ✅ Add note via `/add_note`
  - ✅ Log pomo via `/add_pomo`
  - ✅ Add expense via `/add_expense`
- Added `db_query.py` to view DB state
- Confirmed real-time data insertion from Termux
- Debugged and verified persistence

### 📎 Notes [2025-07-12]

- HTTPie showed perfect JSON formatting and time logs  
- Termux-to-PC sync working well  
- Data confirmed in SQLite from all endpoints  
- DB looks stable enough for GUI hookup  

### 📍 Next Step [2025-07-12]

- Create `api_client.py` wrapper  
- Final push of API updates  
- Begin TUI scaffolding with Textual (2025-07-13)
