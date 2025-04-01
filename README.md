# ajith-kumar-nelliparthi-wasserstoff-AiInternTask

# AI Personal Email Assistant

## Objective: 
Build an AI-powered personal email assistant capable of reading a user's 
Gmail/IMAP inbox, understanding email context, storing emails in a database, and 
interacting with external tools (web search, Slack, calendar) to assist with email actions. 
The assistant should be able to automatically draft or send replies, forward information, 
and schedule events based on email content.

## Day 1: Email Integration with Gmail API

This project is part of a multi-day task to build an AI-powered personal email assistant. On **Day 1**, I implemented email integration using the Gmail API to authenticate and fetch emails from a Gmail inbox. This README outlines the setup process, how to run the script, and what was accomplished.

---

## Objective
- Authenticate with Gmail using OAuth 2.0.
- Fetch and display the latest emails from the inbox (subject, sender, and body).

## Prerequisites
Before running the project, ensure you have the following:
- **Python 3.x**: Installed on your system ([Download](https://www.python.org/downloads/)).
- **Visual Studio Code (VSCode)**: For editing and running the script ([Download](https://code.visualstudio.com/)).
- **Google Cloud Project**: With Gmail API enabled and OAuth credentials set up.
- **Internet Connection**: For API calls and authentication.

## Setup Instructions

### Step 1: Set Up Google Cloud Project
1. **Create a Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Click the project dropdown > **New Project**.
   - Name it (e.g., "EmailAssistant") and click **Create**.

2. **Enable Gmail API**:
   - Navigate to **APIs & Services** > **Library**.
   - Search for "Gmail API" and click **Enable**.

3. **Configure OAuth Consent Screen**:
   - Go to **APIs & Services** > **OAuth consent screen**.
   - Select **External** and click **Create**.
   - Fill in:
     - **App Name**: "Email Assistant"
     - **User Support Email**: Your email
     - **Developer Contact**: Your email
   - Save and continue through the screens.
   - Add scopes: `https://www.googleapis.com/auth/gmail.readonly` and `https://www.googleapis.com/auth/gmail.send`.
   - Add your email as a **Test User** under the **Test users** section.

4. **Create OAuth Credentials**:
   - Go to **APIs & Services** > **Credentials**.
   - Click **+ Create Credentials** > **OAuth 2.0 Client ID**.
   - Set **Application type** to **Desktop app**.
   - Name it (e.g., "Email Assistant Desktop") and click **Create**.
   - Download the `credentials.json` file and save it in your project folder (e.g., `src/`).

### Step 2: Set Up Your Local Environment
1. **Open Project in VSCode**:
   - Open VSCode and select **File > Open Folder**.
   - Choose your project folder (e.g., `C:\aiintern\ajith-kumar-nelliparthi-wasserstoff-AiInternTask\src`).

2. **Create a Virtual Environment**:
   - Open a terminal in VSCode (`Ctrl+``) or use Command Prompt.
   - Run:
     ```bash
     python -m venv .venv
     ```
   - Activate it:
     - Windows: `.venv\Scripts\activate`
     - macOS/Linux: `source .venv/bin/activate`

3. **Install Dependencies**:
   - With the virtual environment active, run:
     ```bash
     pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

### Step 3: Run the Script
1. **Prepare the Script**:
   - Ensure `day_01_email_integration.py` is in your project folder with `credentials.json`.
   - The script authenticates with Gmail and fetches the latest 10 emails.

2. **Execute**:
   - In the terminal (with the virtual environment active):
     ```bash
     python day_01_email_integration.py
     ```
   - First run: A browser window opens for authentication. Log in with your Google account (added as a test user), approve permissions, and close the window when prompted.
   - Subsequent runs: Uses `token.json` for authentication without a browser prompt.

3. **Output**:
   - Prints the subject, sender, and first 100 characters of the body for each email.

## What Was Completed
- **Authentication**: Successfully set up OAuth 2.0 with Gmail API using `credentials.json` and saved tokens in `token.json`.
- **Email Fetching**: Retrieved the latest 20 emails from the inbox, parsed their subject, sender, and body, and displayed them in the terminal.

## Project Structure
```
src/
├── day_01_email_integration.py  # Main script for email integration
├── credentials.json             # Google Cloud OAuth credentials
├── token.json                   # Auto-generated after first authentication
└── requiements.txt
└── README.md                    
```