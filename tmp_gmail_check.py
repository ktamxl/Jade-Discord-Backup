#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import base64
import re

# OAuth credentials
CLIENT_ID = "227784428112-0ies0vm0ad6slf14jc1oqp70m94732fh.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//05jYy_Ale00w3CgYIARAAGAUSNwF-L9IrSWrGSS3R5qTJ33Z-YIc8eHOvVNPV809albtGNvI7swxk8D8ekaN0yXsHmfm9QQlayUU"

# Step 1: Get access token
token_data = urllib.parse.urlencode({
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN,
    "grant_type": "refresh_token"
}).encode()

req = urllib.request.Request("https://oauth2.googleapis.com/token", data=token_data, method="POST")
with urllib.request.urlopen(req) as resp:
    token_resp = json.loads(resp.read())

access_token = token_resp.get("access_token")
print(f"Got access token: {access_token[:30]}...")

def gmail_get(path, params=None):
    base = "https://gmail.googleapis.com/gmail/v1/users/me"
    url = base + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

# Search for Slack credential emails from Travis or Vanessa
queries = [
    "from:travis@excel-plumbing.com xoxb-",
    "from:vanessa@excel-plumbing.com xoxb-",
    "from:travis@excel-plumbing.com slack bot token",
    "from:vanessa@excel-plumbing.com slack bot token",
    "from:travis@excel-plumbing.com slack",
    "from:vanessa@excel-plumbing.com slack",
]

all_msg_ids = set()
for q in queries:
    try:
        result = gmail_get("/messages", {"q": q, "maxResults": 10})
        msgs = result.get("messages", [])
        print(f"Query '{q}': {len(msgs)} results")
        for m in msgs:
            all_msg_ids.add(m["id"])
    except Exception as e:
        print(f"Query '{q}' error: {e}")

print(f"\nTotal unique message IDs found: {len(all_msg_ids)}")

if not all_msg_ids:
    print("NO_SLACK_EMAIL_FOUND")
else:
    # Fetch full content of each message
    for msg_id in all_msg_ids:
        print(f"\n--- Fetching message {msg_id} ---")
        try:
            msg = gmail_get(f"/messages/{msg_id}", {"format": "full"})
            
            # Extract headers
            headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
            print(f"From: {headers.get('From', 'unknown')}")
            print(f"Subject: {headers.get('Subject', 'unknown')}")
            print(f"Date: {headers.get('Date', 'unknown')}")
            
            # Extract body
            def extract_body(payload):
                body = ""
                if "body" in payload and payload["body"].get("data"):
                    body += base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8", errors="replace")
                if "parts" in payload:
                    for part in payload["parts"]:
                        body += extract_body(part)
                return body
            
            body = extract_body(msg.get("payload", {}))
            print(f"Body preview (first 2000 chars):\n{body[:2000]}")
            
            # Look for Slack credentials patterns
            bot_token = re.findall(r'xoxb-[A-Za-z0-9\-]+', body)
            signing_secret = re.findall(r'[0-9a-f]{32}', body)
            workspace_url = re.findall(r'https://[a-zA-Z0-9\-]+\.slack\.com', body)
            channel = re.findall(r'#[a-zA-Z0-9\-_]+', body)
            
            print(f"\nExtracted credentials:")
            print(f"  Bot tokens: {bot_token}")
            print(f"  Potential signing secrets (32-char hex): {signing_secret}")
            print(f"  Workspace URLs: {workspace_url}")
            print(f"  Channels: {channel}")
            
        except Exception as e:
            print(f"Error fetching message {msg_id}: {e}")
