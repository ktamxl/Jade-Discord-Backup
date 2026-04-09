#!/usr/bin/env python3
"""Check payables@excel-plumbing.com inbox for Slack credentials from Travis or Vanessa."""

import requests
import json
import base64
import re

# OAuth credentials
CLIENT_ID = "227784428112-0ies0vm0ad6slf14jc1oqp70m94732fh.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//05jYy_Ale00w3CgYIARAAGAUSNwF-L9IrSWrGSS3R5qTJ33Z-YIc8eHOvVNPV809albtGNvI7swxk8D8ekaN0yXsHmfm9QQlayUU"

def get_access_token():
    resp = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
        "grant_type": "refresh_token"
    })
    data = resp.json()
    if "access_token" not in data:
        print(f"ERROR getting token: {data}")
        return None
    print(f"Access token: {data['access_token'][:20]}...")
    return data["access_token"]

def decode_body(payload):
    """Recursively extract text body from email payload."""
    text = ""
    if payload.get("mimeType") == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            text += base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    elif payload.get("mimeType") == "text/html":
        data = payload.get("body", {}).get("data", "")
        if data:
            text += base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    for part in payload.get("parts", []):
        text += decode_body(part)
    return text

def get_header(headers, name):
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return ""

def check_inbox():
    token = get_access_token()
    if not token:
        return

    headers = {"Authorization": f"Bearer {token}"}
    base_url = "https://gmail.googleapis.com/gmail/v1/users/me"

    # First check: look for xoxb- tokens in inbox
    print("\n=== Searching for xoxb tokens ===")
    search_resp = requests.get(
        f"{base_url}/messages",
        params={"q": "xoxb", "maxResults": 10},
        headers=headers
    )
    xoxb_data = search_resp.json()
    print(f"xoxb search: {json.dumps(xoxb_data, indent=2)}")

    xoxb_messages = xoxb_data.get("messages", [])

    # Second check: recent messages from Travis or Vanessa
    print("\n=== Searching for emails from Travis/Vanessa ===")
    search_resp2 = requests.get(
        f"{base_url}/messages",
        params={"q": "from:(travis@excel-plumbing.com OR vanessa@excel-plumbing.com)", "maxResults": 5},
        headers=headers
    )
    tv_data = search_resp2.json()
    tv_messages = tv_data.get("messages", [])
    print(f"Travis/Vanessa messages found: {len(tv_messages)}")

    # Check the xoxb messages first
    slack_credentials = None
    for msg_info in xoxb_messages:
        msg_id = msg_info["id"]
        msg_resp = requests.get(f"{base_url}/messages/{msg_id}?format=full", headers=headers)
        msg = msg_resp.json()
        hdrs = msg.get("payload", {}).get("headers", [])
        from_addr = get_header(hdrs, "From")
        subject = get_header(hdrs, "Subject")
        date = get_header(hdrs, "Date")
        print(f"\n--- xoxb Message ---")
        print(f"From: {from_addr}")
        print(f"Subject: {subject}")
        print(f"Date: {date}")

        body = decode_body(msg.get("payload", {}))
        print(f"Body (first 500 chars): {body[:500]}")

        # Check if from Travis or Vanessa
        from_lower = from_addr.lower()
        if "travis@excel-plumbing.com" in from_lower or "vanessa@excel-plumbing.com" in from_lower:
            print(">>> FROM TRAVIS OR VANESSA - checking for credentials!")
            # Extract bot token
            bot_token_match = re.search(r'xoxb-[A-Za-z0-9\-]+', body)
            signing_secret_match = re.search(r'(?:signing.?secret|secret)[\s:=]+([a-f0-9]{32,})', body, re.IGNORECASE)
            workspace_match = re.search(r'https://[a-zA-Z0-9\-]+\.slack\.com', body)
            channel_match = re.search(r'(?:channel|#)[\s:]*([#]?[a-zA-Z0-9\-_]+)', body, re.IGNORECASE)

            if bot_token_match:
                slack_credentials = {
                    "bot_token": bot_token_match.group(0),
                    "signing_secret": signing_secret_match.group(1) if signing_secret_match else None,
                    "workspace_url": workspace_match.group(0) if workspace_match else None,
                    "channel": channel_match.group(1) if channel_match else None,
                    "from": from_addr,
                    "subject": subject,
                    "date": date,
                    "body": body
                }
                print(f"FOUND CREDENTIALS: {slack_credentials}")
                break

    # Also check most recent Travis/Vanessa email
    print(f"\n=== Checking most recent Travis/Vanessa emails ===")
    for msg_info in tv_messages[:3]:
        msg_id = msg_info["id"]
        msg_resp = requests.get(f"{base_url}/messages/{msg_id}?format=full", headers=headers)
        msg = msg_resp.json()
        hdrs = msg.get("payload", {}).get("headers", [])
        from_addr = get_header(hdrs, "From")
        subject = get_header(hdrs, "Subject")
        date = get_header(hdrs, "Date")
        print(f"\n--- Message ---")
        print(f"From: {from_addr}")
        print(f"Subject: {subject}")
        print(f"Date: {date}")

        body = decode_body(msg.get("payload", {}))
        # Check if body contains Slack-related content
        if "xoxb" in body or "slack" in body.lower() or "signing" in body.lower():
            print(f"Body contains Slack content! (first 1000 chars):\n{body[:1000]}")
            if slack_credentials is None:
                bot_token_match = re.search(r'xoxb-[A-Za-z0-9\-]+', body)
                if bot_token_match:
                    signing_secret_match = re.search(r'(?:signing.?secret|secret)[\s:=]+([a-f0-9]{32,})', body, re.IGNORECASE)
                    workspace_match = re.search(r'https://[a-zA-Z0-9\-]+\.slack\.com', body)
                    channel_match = re.search(r'(?:channel|#)[\s:]*([#]?[a-zA-Z0-9\-_]+)', body, re.IGNORECASE)
                    slack_credentials = {
                        "bot_token": bot_token_match.group(0),
                        "signing_secret": signing_secret_match.group(1) if signing_secret_match else None,
                        "workspace_url": workspace_match.group(0) if workspace_match else None,
                        "channel": channel_match.group(1) if channel_match else None,
                        "from": from_addr,
                        "subject": subject,
                        "date": date,
                        "body": body
                    }
        else:
            print(f"Body preview: {body[:200]}")

    # Output final result
    print("\n=== FINAL RESULT ===")
    if slack_credentials:
        print("CREDENTIALS FOUND!")
        print(json.dumps({k: v for k, v in slack_credentials.items() if k != "body"}, indent=2))
        # Save to file for further processing
        with open("/workspace/memory/slack_credentials_found.json", "w") as f:
            json.dump(slack_credentials, f, indent=2)
        print("Saved to /workspace/memory/slack_credentials_found.json")
    else:
        print("NO SLACK CREDENTIALS FOUND IN INBOX")

if __name__ == "__main__":
    check_inbox()
