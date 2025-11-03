import sqlite3, json

DB = "/nfs/demo.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("SELECT id FROM contacts")
ids = [row[0] for row in cur.fetchall()]

with open("/nfs/security_snapshot.json", "w") as f:
    json.dump(ids, f)

conn.close()
print("Snapshot saved.")
