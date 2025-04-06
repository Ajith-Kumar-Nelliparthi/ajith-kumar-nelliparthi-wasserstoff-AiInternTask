# ajith-kumar-nelliparthi-wasserstoff-AiInternTask

# AI Personal Email Assistant

## Objective: 
Build an AI-powered personal email assistant capable of reading a user's 
Gmail/IMAP inbox, understanding email context, storing emails in a database, and 
interacting with external tools (web search, Slack, calendar) to assist with email actions. 
The assistant should be able to automatically draft or send replies, forward information, 
and schedule events based on email content.

## Features
- **Day 1-2: Email Parsing & Storage**: Parses Gmail emails and stores them in `emails.db`.
- **Day 3: Context Understanding**: Summarizes email threads and infers intent using BART and DistilBERT.
- **Day 4: Web Search**: Answers email queries with web search results.
- **Day 5: Slack Notifications**: Sends updates to Slack channels.
- **Day 5: Calendar Scheduling**: Detects scheduling intent and creates Google Calendar events.
- **Day 6: Automated Replies**: Drafts and sends email replies, with auto-send for trusted senders and manual confirmation otherwise.

## Project Structure
```
src/
├── day_01_email_integration.py  # Main script for email integration
├── gmail_auth.py                # OAuth 2.0 authentication class
├── day_02_email_parsing_storing.py  # Day 2 Script
├── email_analyzer.py                # context understanding with LLM
├── web_search_assistant.py          # Web search with Google Custom Search API
├── slack_notifier.py               # Slack notification integration 
├── calendar_scheduler.py           # Calendar scheduling integration
├── email_drafter.py                # Automated reply generation
├── credentials.json               # Google Cloud OAuth credentials
├── token.json                     # Auto-generated after first 
├── emails.db                      # sqlite database
└── requiements.txt                # pip requirements
└── README.md                    
```


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

## Day 2: Email Parsing and Storage

## Objective
- Parse essential email fields (sender, recipient, subject, timestamp, body, attachments).
- Store parsed data in an SQLite database with threading support.

## What Was Completed
- **Parsing**: Extracted sender, recipient, subject, timestamp, body, and attachments from Gmail messages.
- **Storage**: Created an SQLite database (`emails.db`) with tables for emails and attachments.
- **Threading**: Used `threadId` to link replies to original emails.
- **Class-Based Design**: Implemented `EmailManager` class for modularity.

## Setup Instructions
- Same as Day 1 (see above).
- No additional libraries required beyond Day 1 setup.

## Running the Script
1. Place `day_02_email_parsing_storing.py` in the `src/` folder with `credentials.json`.
2. Run:
   ```bash
   python day_02_email_parsing_storing.py

## Day 3: Email Analyzer and Web Search

### Objectives
1. **Context Understanding with LLM**: Use a Transformer-based model to summarize email threads and infer intent.
2. **Web Search Integration**: Add web search capability to answer email queries using Google Custom Search API.

### What Was Completed

- **Task 3: EmailAnalyzer Class** (`email_analyzer.py`):
  - **Implementation**: Uses `facebook/bart-large-cnn` for summarization and `distilbert-base-uncased-finetuned-sst-2-english` for intent inference (sentiment-based).
  - **Functionality**: Summarizes email threads and infers intent (e.g., confirmation, request) from `emails.db`.
  - **Limitations**:
    - **Lack of Accuracy**: The intent inference relies on sentiment (POSITIVE/NEGATIVE), which isn’t precise for email-specific intents (e.g., distinguishing confirmation from rejection). The example output labeled "Your application has been submitted. Good luck!" as "negative," likely misinterpreting neutral content.
    - **Time-Consuming**: Downloading large models (e.g., 1.63 GB for BART) and running on CPU is slow (5–15 minutes for initial setup, plus processing time).
  - **Alternative**: If you have an OpenAI API key, you can replace the Transformer-based approach with GPT-3.5/4 for faster, more accurate intent detection and summarization. Modify `email_analyzer.py` to use the OpenAI client library instead of `transformers`.

- **Task 4: WebSearchAssistant Class** (`web_search_assistant.py`):
  - Integrates Google Custom Search API to answer email questions.
  - Filters results by detecting queries in email content.

### Setup Instructions
- **General Dependencies**:
  ```bash
  pip install google-api-python-client html2text

### Task 3 (Context Understanding):
Install:
```
pip install transformers torch
```

Note: Initial run downloads large models (~1.9 GB total), requiring significant time and disk space.

Optional (OpenAI): If using GPT, install openai:
```
pip install openai
```
Update email_analyzer.py with your API key and GPT calls.

For Task 4:
Get Google Custom Search API key and CX ID from [Google Cloud Console](https://console.cloud.google.com/) and [cse.google.com](https://programmablesearchengine.google.com/controlpanel/all).

Update web_search_assistant.py with your API key and CX ID.



### Running the Scripts
1. Context Understanding:
```
   python email_analyzer.py
```
Analyzes a hardcoded thread/email (e.g., '195f5fe2b09c8fd1').

Output example:

![alt text](<Screenshot 2025-04-03 113246.png>)

![alt text](<Screenshot 2025-04-03 113901.png>)

2. Web Search
```
python web_search_assistant.py
```
Processes a hardcoded email (e.g., '195f6012a4f6f310') for queries.

Output example:

![alt text](<Screenshot 2025-04-03 150240.png>)


## Day 4: Slack Integration

### Objective
- **Tool Integration – Slack**: Integrate Slack’s API to forward notifications about important emails to a workspace/channel/user using `chat.postMessage`.

### What Was Completed
- **Task5: SlackNotifier Class** (`slack_notifier.py`):
  - **Implementation**: Uses Slack Web API via `slack-sdk` to send messages with a bot token.
  - **Functionality**: 
    - Identifies "important" emails based on sender (e.g., `@indeed.com`) or subject keywords (e.g., "urgent").
    - Sends a Slack message to a specified channel with email sender, subject, summary (from `EmailAnalyzer`), intent, and body snippet.
  - **Security**: Bot token stored in `.env`, not hardcoded.
  - **OAuth Scope**: Requires `chat:write` for the Slack bot.

Slack Configuration:
- Create a Slack app at [api.slack.com/apps](https://api.slack.com/apps):
   - Name: "EmailAssistantBot", Workspace: Your workspace.

- Add scope: OAuth & Permissions > Scopes > Bot Token Scopes > chat:write.

- Install app to workspace, copy Bot User OAuth Token (e.g., xoxb-...).

- Invite bot to channel (e.g., /invite @EmailAssistantBot in #general).
- Update .env
```
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX_ID=your_cx_id
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
```
### Running the Script
- Slack Notification:
```
   python slack_notifier.py
```

- Sends a notification to ```#general``` (or your specified channel) for email 195fafee3c89c982 if deemed important.

Output example:
![alt text](<Screenshot 2025-04-04 153211.png>)


## Day 5: Calendar Integration
- **Objective**: Incorporate Google Calendar scheduling to detect meeting-related emails and create events.
- **Task: CalendarScheduler Class** (`calendar_scheduler.py`):
  - **Implementation**: Uses Google Calendar API to create events; leverages `EmailAnalyzer` for intent detection.
  - **Functionality**:
    - Detects scheduling intent (e.g., "meeting on Friday") with keywords and basic parsing.
    - Extracts event details (title, date, time) and adds a 1-hour event to the primary calendar.
  - **Limitations**: Basic parsing is rudimentary; enhance with OpenAI GPT for precise extraction.
  - **Authentication**: Reuses `GmailAuthenticator` with added Calendar scope.

1. Enable Google Calendar API:
- In Google Cloud Console, select email-assistant.
- Enable "Google Calendar API".

2. Update OAuth Scopes:
- Go to APIs & Services > OAuth consent screen.
- Click Edit App, go to Data Access or Scopes.
- Click Add or Remove Scopes, add ```https://www.googleapis.com/auth/calendar.events```.
- Save changes.

3. Update credentials.json:
- In APIs & Services > Credentials, download updated OAuth 2.0 Client ID.
- Replace src/credentials.json.

4. Re-authenticate:
- Delete src/token.json
``` del src\token.json```
- Run any script (e.g., calendar_scheduler.py) to re-authenticate with new scopes.

5. Update gmail_auth.py:
- Added scope:
``` 
self.SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/calendar.events'
]
```

### Running the Scripts

``` python calendar_scheduler.py ```
` Creates an event for email 195fafee3c89c982 if scheduling intent is detected.

Output example:
![alt text](<Screenshot 2025-04-05 212219.png>)


## Day 6: Automated Reply Generation

### Objective
- **Automated Reply Generation**: Draft and send replies for emails the assistant can handle (e.g., scheduling requests).

### What Was Completed
- **Task: EmailDrafter Class** (`email_drafter.py`):
  - **Implementation**: Uses Gmail API to send replies, `CalendarScheduler` to book meetings, and `EmailAnalyzer` for intent and drafting.
  - **Functionality**:
    - Detects reply-worthy emails (e.g., scheduling requests).
    - Drafts polite responses with LLM (proposes meeting times if booked).
    - Sends via Gmail API with safeguards: auto-send for safe senders, logs to `replies.log`, and prompts confirmation otherwise.
  - **Safeguards**: Whitelist (`safe_senders`), logging, and manual confirmation for non-safe cases.

### Setup Instructions
- **Dependencies**: Same as previous days (`google-api-python-client`, `transformers`, `torch`, etc.).
- **Gmail API**:
  - Scope `https://www.googleapis.com/auth/gmail.send` already added in `gmail_auth.py`.
  - Re-authenticate if needed:
    ```bash
    del src\token.json
    python email_drafter.py
    ```
- **Update `emails.db`** (for testing):
  ```bash
  sqlite3 src/emails.db "UPDATE emails SET body = 'Please schedule a meeting on Friday at 2pm' WHERE id = '195fafee3c89c982';"

### Running the Script
- Draft and Send Reply:
```bash
python email_drafter.py
```
- Checks email 195fafee3c89c982, drafts a reply, and prompts for confirmation unless sender is in safe_senders.

Output example:
![alt text](<Screenshot 2025-04-06 100920.png>)

