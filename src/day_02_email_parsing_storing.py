# import libraries

import os
import base64 # For encoding and decoding email content
import sqlite3
from datetime import datetime
from googleapiclient.discovery import Resource  # For Google API service
from gmail_auth import GmailAuthenticator 

class EmailManager:
    """class to manage email parsing and storing"""

    def __init__(self, db_path='emails.db'):
        """Initialize the EmailManager with a database path."""
        self.conn = sqlite3.connect(db_path)
        self.setup_database()
    
    def setup_database(self):
        c = self.conn.cursor()
        # EMAILS TABLE WITH THREADING SUPPORT
        c.execute('''CREATE TABLE IF NOT EXISTS emails (
                    id TEXT PRIMARY KEY,
                    thread_id TEXT,
                    sender TEXT,
                    recipient TEXT,
                    subject TEXT,
                    timestamp INTEGER,
                    body TEXT)''')
        # ATTACHMENTS TABLE
        c.execute('''CREATE TABLE IF NOT EXISTS attachments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message_id TEXT,
                    filename TEXT,
                    mime_type TEXT,
                    size INTEGER,
                    FOREIGN KEY(message_id) REFERENCES emails(id))''')
        self.conn.commit()

    def parse_email(self, service, message):
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
        headers = msg['payload']['headers']

        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        recipient = next((h['value'] for h in headers if h['name'] == 'To'), 'Unknown Recipient')
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        timestamp = int(msg.get('internalDate', 0)) // 1000  # Convert to seconds
        thread_id = msg.get('threadId', message['id'])  # Use threadId if available, else use message id

        body = ''
        if 'parts' in msg['payload']:
            for part in msg['payload']['parts']:
                if part['mimeType'] == 'text/plain' and 'data' in part['body']:
                    body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                    break
                elif 'data' in msg['payload']['body']:
                    body = base64.urlsafe_b64decode(msg['payload']['body']['data']).decode('utf-8')

                attachments = []
                if 'parts' in msg['payload']:
                    for part in msg['payload']['parts']:
                        if 'filename' in part and part['filename']:
                            attachments.append({
                                'filename': part['filename'],
                                'mime_type': part['mimeType'],
                                'size': int(part['body'].get('size', 0)),
                            })
                return {
                    'id': message['id'],
                    'thread_id': thread_id,
                    'sender': sender,
                    'recipient': recipient,
                    'subject': subject,
                    'timestamp': timestamp,
                    'body': body,
                    'attachments': attachments
                }
    def store_email(self, email):
        """store a parsed email and its attachments in the database"""
        c = self.conn.cursor()
        c.execute('''INSERT OR REPLACE INTO emails (id, thread_id, sender, recipient, subject, timestamp, body)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                    (email['id'], email['thread_id'], email['sender'], email['recipient'],
                     email['subject'], email['timestamp'], email['body']))
        for attachment in email['attachments']:
            c.execute('''INSERT INTO attachments (message_id, filename, mime_type, size)
                        VALUES (?, ?, ?, ?)''', 
                        (email['id'], attachment['filename'], attachment['mime_type'], attachment['size']))
        self.conn.commit()

    def fetch_and_store_emails(self, service, max_results=10):
        """fetch emails from the Gmail API and store them in the database"""
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])
        
        for message in messages:
            email = self.parse_email(service, message)
            if email:
                self.store_email(email)
                self.print_email(email)
    
    def print_email(self, email):
        """Print email details for verification."""
        print(f"ID: {email['id']}")
        print(f"Thread ID: {email['thread_id']}")
        print(f"From: {email['sender']}")
        print(f"To: {email['recipient']}")
        print(f"Subject: {email['subject']}")
        print(f"Timestamp: {datetime.fromtimestamp(email['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Body: {email['body'][:100]}...")
        if email['attachments']:
            print("Attachments:")
            for att in email['attachments']:
                print(f" - {att['filename']} ({att['mime_type']}, {att['size']} bytes)")
        print()

    def close(self):
        """Close the database connection."""
        self.conn.close()

if __name__ == "__main__":
    auth = GmailAuthenticator()
    service = auth.get_service()
    email_manager = EmailManager()
    email_manager.fetch_and_store_emails(service)
    email_manager.close()


