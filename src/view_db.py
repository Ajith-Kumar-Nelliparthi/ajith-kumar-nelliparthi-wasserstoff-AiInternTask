import sqlite3

# Connect to the database
conn = sqlite3.connect('emails.db')
c = conn.cursor()

# View emails table
print("Emails Table:")
c.execute("SELECT * FROM emails")
for row in c.fetchall():
    print(row)

# View attachments table
print("\nAttachments Table:")
c.execute("SELECT * FROM attachments")
for row in c.fetchall():
    print(row)

# Close connection
conn.close()