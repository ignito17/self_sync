# tui_dashboard.py

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal

from modules import diary_logger
import sqlite3

# ✅ Point to the correct unified DB
DB_PATH = "db/data.sqlite"

# ✅ Fetch structured, correct data from tables
def fetch_latest_data():
    diary_logger.init_db()  # Ensure tables exist

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 📝 Fetch latest 5 diary entries
    try:
        c.execute("SELECT title, description FROM diary_entries ORDER BY timestamp DESC LIMIT 25")
        notes = c.fetchall()
    except sqlite3.OperationalError:
        notes = []

    # ⏱️ Total pomodoro minutes
    try:
        c.execute("SELECT SUM(minutes) FROM pomo_sessions")
        pomo_total = c.fetchone()[0] or 0
    except sqlite3.OperationalError:
        pomo_total = 0

    # 💸 Total expenses
    try:
        c.execute("SELECT SUM(amount) FROM expenses")
        expenses_total = c.fetchone()[0] or 0.0
    except sqlite3.OperationalError:
        expenses_total = 0.0

    conn.close()
    return notes, pomo_total, expenses_total

# 🎨 TUI Application Class
class SelfSyncDashboard(App):
    def compose(self) -> ComposeResult:
        notes, pomo_total, expenses_total = fetch_latest_data()

        # 🧾 Format notes block
        if notes:
            notes_text = "\n".join(f"- {title.strip()[:20]}: {desc.strip()[:40]}" for title, desc in notes)
        else:
            notes_text = "No notes found."

        pomo_text = f"{pomo_total} minutes"
        expense_text = f"₹{expenses_total:.2f}"

        # 🖼️ Build UI
        yield Header()
        yield Horizontal(
            Static(f"📝 Notes\n{notes_text}", expand=True),
            Static(f"⏱️ Pomodoro\n{pomo_text}", expand=True),
            Static(f"💸 Expenses\n{expense_text}", expand=True),
        )
        yield Footer()

# 🏃 Run the TUI
if __name__ == "__main__":
    SelfSyncDashboard().run()
