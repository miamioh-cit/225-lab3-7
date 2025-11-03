# 
import sqlite3, json, os

DB = "/nfs/demo.db"
SNAPSHOT = "/nfs/security_snapshot.json"

if not os.path.exists(SNAPSHOT):
    print("No snapshot file found; skipping cleanup.")
    exit(0)

with open(SNAPSHOT, "r") as f:
    baseline_ids = set(json.load(f))

conn = sqlite3.connect(DB)
cur = conn.cursor()

# Get all current contact IDs
cur.execute("SELECT id FROM contacts")
current_ids = {row[0] for row in cur.fetchall()}

# Security scan created these:
new_ids = current_ids - baseline_ids

if new_ids:
    cur.executemany("DELETE FROM contacts WHERE id = ?", [(i,) for i in new_ids])
    print(f"Removed {len(new_ids)} security-created contacts.")
else:
    print("No security-created contacts to remove.")

conn.commit()
conn.close()
