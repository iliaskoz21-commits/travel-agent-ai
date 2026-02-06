import sqlite3
# Η νέα διαδρομή για το import στην έκδοση 0.2+
from langgraph.checkpoint.sqlite import SqliteSaver 

def get_sqlite_memory():
    # Δημιουργία σύνδεσης
    conn = sqlite3.connect("travel_memory.db", check_same_thread=False)
    return SqliteSaver(conn)