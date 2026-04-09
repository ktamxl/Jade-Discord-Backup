import urllib.request
import urllib.parse
import json
import base64
import re

# Read credentials from file
with open("/workspace/memory/gmail_oauth_credentials.md", "r") as f:
    creds_content = f.read()

# Extract credentials
client_id_match = re.search(r'CLIENT_ID=(\S+)', creds_content)
client_secret_match = re.search(r'CLIENT_SECRET=(\S+)', creds_content)
refresh_token_match = re.search(r'REFRESH_TOKEN=(\S+)', creds_content)

CLIENT_ID = client_id_match.group(1)
CLIENT_SECRET = client_secret_match.group(1)
REFRESH_TOKEN = refresh_token_match.group(1)

print(f"Client ID: {CLIENT_ID[:30]}...")
print(f"Refresh token length: {len(REFRESH_TOKEN)}")
print(f"Refresh token prefix: {REFRESH_TOKEN[:20]}...")

# Step 1: Get fresh access token
token_params = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "refresh_token": REFRESH_TOKEN,
    "grant_type": "refresh_token"
}
token_data = urllib.parse.urlencode(token_params).encode("utf-8")
req = urllib.request.Request(
    "https://oauth2.googleapis.com/token",
    data=token_data,
    method="POST",
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
try:
    with urllib.request.urlopen(req) as resp:
        token_resp = json.load(resp)
    access_token = token_resp["access_token"]
    print(f"Access token acquired successfully.")
except Exception as e:
    print(f"Error getting token: {e}")
    if hasattr(e, 'read'):
        print(f"Error body: {e.read().decode()}")
    raise

# Step 2: Search Gmail for Slack credentials from Travis or Vanessa
queries = [
    'from:travis@excel-plumbing.com xoxb',
    'from:vanessa@excel-plumbing.com xoxb',
    'from:travis@excel-plumbing.com "slack"',
    'from:vanessa@excel-plumbing.com "slack"',
    'from:travis@excel-plumbing.com "signing secret"',
    'from:vanessa@excel-plumbing.com "signing secret"',
]

message_ids = set()
for q in queries:
    encoded_q = urllib.parse.quote(q)
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?q={encoded_q}&maxResults=5"
    req2 = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
    with urllib.request.urlopen(req2) as resp2:
        result = json.load(resp2)
    msgs = result.get("messages", [])
    print(f"Query '{q}': {len(msgs)} messages found")
    for m in msgs:
        message_ids.add(m["id"])

print(f"\nTotal unique messages to check: {len(message_ids)}")

if not message_ids:
    print("RESULT: NO_SLACK_CREDENTIALS_FOUND")
else:
    found_credentials = {}
    
    # Fetch each message and look for Slack credentials
    for msg_id in message_ids:
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{msg_id}?format=full"
        req3 = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})
        with urllib.request.urlopen(req3) as resp3:
            msg = json.load(resp3)
        
        # Get headers
        headers_dict = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}
        subject = headers_dict.get("Subject", "")
        sender = headers_dict.get("From", "")
        date = headers_dict.get("Date", "")
        print(f"\nMessage: {msg_id}")
        print(f"  From: {sender}")
        print(f"  Subject: {subject}")
        print(f"  Date: {date}")
        
        # Extract body recursively
        def get_body(payload):
            body = ""
            mime_type = payload.get("mimeType", "")
            if "text" in mime_type and payload.get("body", {}).get("data"):
                try:
                    body += base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8", errors="replace")
                except:
                    pass
            for part in payload.get("parts", []):
                body += get_body(part)
            return body
        
        body = get_body(msg.get("payload", {}))
        print(f"  Body length: {len(body)} chars")
        print(f"  Body preview:\n{body[:800]}")
        
        # Look for Slack bot token (xoxb-)
        xoxb_match = re.search(r'xoxb-[\w-]+', body)
        if xoxb_match:
            bot_token = xoxb_match.group()
            print(f"\n  *** BOT TOKEN FOUND: {bot_token[:20]}...")
            found_credentials['bot_token'] = bot_token
        
        # Look for signing secret (32-char hex string near "signing" or "secret")
        secret_patterns = [
            r'(?:signing.?secret|secret).{0,50}([a-f0-9]{32})',
            r'([a-f0-9]{32}).{0,30}(?:signing.?secret|secret)',
        ]
        for pat in secret_patterns:
            sm = re.search(pat, body, re.IGNORECASE)
            if sm:
                signing_secret = sm.group(1)
                print(f"\n  *** SIGNING SECRET FOUND: {signing_secret[:10]}...")
                found_credentials['signing_secret'] = signing_secret
                break
        
        # Look for workspace URL
        ws_match = re.search(r'https?://[\w-]+\.slack\.com', body)
        if ws_match:
            workspace_url = ws_match.group()
            print(f"\n  *** WORKSPACE URL FOUND: {workspace_url}")
            found_credentials['workspace_url'] = workspace_url
        
        # Look for channel name
        ch_match = re.search(r'(?:channel|#)([\w-]+)', body, re.IGNORECASE)
        if ch_match:
            channel_name = ch_match.group(1)
            print(f"\n  *** CHANNEL NAME FOUND: {channel_name}")
            found_credentials.setdefault('channel_name', channel_name)
    
    print(f"\n\nFINAL RESULT: {json.dumps(found_credentials, indent=2)}")
    if 'bot_token' in found_credentials:
        print("CREDENTIALS_FOUND=TRUE")
    else:
        print("RESULT: NO_BOT_TOKEN_IN_MESSAGES")
