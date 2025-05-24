import sqlite3
print(sqlite3.version)
conn = sqlite3.connect(":memory:")
print("Connected!")
conn.close()