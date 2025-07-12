import os
import re
from datetime import datetime

# 📁 Relative to script location: self_sync/docs/track/scripts/update_today.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # resolves to /docs/track
TODAY_PATH = os.path.join(BASE_DIR, "today.md")
LOG_DIR = os.path.join(BASE_DIR, "logs")

def extract_day_blocks(content):
    pattern = r"(## 📆 (\d{4}-\d{2}-\d{2})[\s\S]+?)(?=\n## 📆 |\Z)"
    return re.findall(pattern, content)

def extract_next_step(block):
    match = re.search(r"### 📍 Next Step \[\d{4}-\d{2}-\d{2}\]\n\n([\s\S]+?)(?=\n###|\Z)", block)
    return match.group(1).strip() if match else ""

def archive_to_log(date_str, block):
    os.makedirs(LOG_DIR, exist_ok=True)
    path = os.path.join(LOG_DIR, f"{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# 📆 Archived Block: {date_str}\n\n{block.strip()}\n")
    print(f"✅ Archived: {path}")

def create_fresh_today(today_date, carry_focus):
    header = """# 📅 Daily Logs and work tracker

---

## 🔁 Daily Update Logic (auto/manual)

> This logic defines how `today.md` will evolve daily:

- At **day start** (e.g., `2025-07-13`):
  - 🟡 Check `📍 Next Step` in yesterday’s section
  - ✏️ Append pending tasks from `📍 Next Step` to today’s "Focus" or "What I Plan"
  - 📁 Save current `today.md` as `docs/track/logs/YYYY-MM-DD.md`
  - 🆕 Create fresh `today.md` for new date with carried tasks + time budget
  - 🔄 Update `perf_tracker.md` with execution block for day

---"""
    fresh = f"""
## 📆 {today_date} – Self Sync Phase 2, Day N

### 🔧 Focus [{today_date}]

{carry_focus if carry_focus else "Continue development."}

### ⏱️ Time Budget [{today_date}]

~2 hours

### ✅ What I Did [{today_date}]

- (Start your session, fill as you go...)

### 📎 Notes [{today_date}]

- (Your session observations...)

### 📍 Next Step [{today_date}]

- (Plan for tomorrow)
"""
    with open(TODAY_PATH, "w", encoding="utf-8") as f:
        f.write(header + fresh)
    print(f"✅ Created new today.md for {today_date}")

def run_update():
    with open(TODAY_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = extract_day_blocks(content)
    if len(blocks) < 2:
        print("⚠️ Not enough blocks to archive. Need at least 2.")
        return

    yesterday_block, date_yesterday = blocks[-2]
    next_tasks = extract_next_step(yesterday_block)

    archive_to_log(date_yesterday, yesterday_block)

    today_date = str(datetime.now().date())
    create_fresh_today(today_date, next_tasks)

if __name__ == "__main__":
    run_update()
