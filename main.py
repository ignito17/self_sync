# Base CLI Runner for the script 

# self_sync_core-a1			-- file version name
# self_sync/main.py			-- file name

from modules import time_tracker,money_tracker,diary_logger,stats_viewer
import sys

def print_help():
	print("""
Available Commands:
	pomo <minutes> <topic>			-- Log a PomoDoro Session
	spend <amount> <desc> 			-- Log an expense
	note <title> <desc> 			-- Save a diary note
	review							-- Show today's summary
									-- Please leave no option vacancy
	""")

# time_tracker.init_db()			#legacy from self_sync_core-a1
# money_tracker.init_db()			#legacy from self_sync_core-a1
diary_logger.init_db()


def main():
	if len(sys.argv) < 2:
		print_help()
		print("Please refer help for correct usages")
		return
	cmd=sys.argv[1]
	if cmd=="pomo":
		time_tracker.add_pomo(int(sys.argv[2])," ".join(sys.argv[3:]))
	if cmd=="spend":
		money_tracker.add_expense(float(sys.argv[2])," ".join(sys.argv[3:]))
	elif cmd=="note":
		diary_logger.add_note(str(sys.argv[2])," ".join(sys.argv[3:]))
	elif cmd=="review":
		stats_viewer.show_review()
	else:
		print_help()
if __name__=="__main__":
	main()

