Phase 1: The Core Tracker (TOM – Time, Objective, Money)** with a focus on pragmatic execution inside Termux first. No abstractions for now — just useful, living code.

---

## ✅ Project Self Sync

After considering the execution style and personal integration goals, self_syncis as a name that fits both function and spirit:

### 🔷 `self_sync`

> **“Personal, local sync runtime — managing your time, actions, and resources.”**
> Modular, private, portable. Designed to sync and thus observe *your resources* with your *plans*.

If you'd like alternatives, here are a few in the same spirit:

Architecture wise `self_sync` has:

* A clean UNIX-style feeling
* Meaning tied to your current needs and goals.
* Extensible scope 
	- designed with modularity in mind.
	- (`self_sync_core`, `self_sync_web`, `self_sync_api` etc.)

---

## Self sync Core `self_sync_core-a1`

### 1. 📂 Project Bootstrapping

Set up the basic folder on Termux(initial developed on)/any other unix environment:

```bash
mkdir ~/dev_ignito/self_sync_core-a1
cd ~/dev_ignito/self_sync_core-a1
git init
```

Create this file tree:

```text
self_sync_core-a1/
├── main.py                  # CLI interface to manage your day
├── db/
│   └── data.sqlite          # SQLite for all logs
├── modules/
│   ├── time_tracker.py      # For tracking pomos, chores
│   ├── money_tracker.py     # Expense / income logger
│   ├── diary_logger.py      # Daily notes and action logs
│   └── stats_viewer.py      # Weekly summary etc
├── README.md
```

---

### 2. 📜 First Code: `main.py`

We'll start with a basic CLI runner that calls modules like:

```python
# main.py
from modules import time_tracker, money_tracker, diary_logger, stats_viewer
import sys

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None

    if cmd == "pomo":
        time_tracker.add_pomo(sys.argv[2:])
    elif cmd == "spend":
        money_tracker.add_expense(sys.argv[2:])
    elif cmd == "note":
        diary_logger.add_note(" ".join(sys.argv[2:]))
    elif cmd == "review":
        stats_viewer.show_review()
    else:
        print("Available commands: pomo, spend, note, review")
```

---

### 3. 📦 GitHub Repo Push

Let’s call the repo: `self_sync`
You can create it via:

```bash
gh repo create self_sync --public --description "A personal runtime to manage time, task, money and habits" --source=. --remote=origin --push
```

---

### 4. 🧪 Test With Simulated Logs

Once basic modules are scaffolded, you’ll:

* Add 2-3 pomos/day via Termux
* Log 1-2 expenses
* Write 1 short note
* Review day at night

This will be your living proof of concept.

---

## 🧭 Final Alignment

🔹 Name: `self_sync`
🔹 Host: Termux-first, Linux-compatible
🔹 Primary: CLI now, optional TUI or Web later
🔹 Version 0 Goal: Reliable tracker for time, notes, and money

---

---- Initial Iteration of the Application.
