import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class GmailAuthenticator:
    """Class to handle Gmail API authentication."""

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
              'https://www.googleapis.com/auth/gmail.send']

    def __init__(self, credentials_path='credentials.json', token_path='token.json'):
        """Initialize with paths to credentials and token files."""
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticate with Gmail API and build the service."""
        creds = None
        # Load existing token if available
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        
        # If no valid credentials, refresh or create new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=8080)
                # Save the credentials for future use
                with open(self.token_path, 'w') as token:
                    token.write(creds.to_json())
        
        # Build and store the Gmail service
        self.service = build('gmail', 'v1', credentials=creds)

    def get_service(self):
        """Return the authenticated Gmail service."""
        return self.service

if __name__ == '__main__':
    # Test the class
    auth = GmailAuthenticator()
    service = auth.get_service()
    print("Authentication successful!")