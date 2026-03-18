#!/usr/bin/env python3
"""Check payables inbox for Slack credentials from Travis or Vanessa."""

import urllib.request
import urllib.parse
import json
import base64
import re

# OAuth credentials
CLIENT_ID = '227784428112-0ies0vm0ad6slf14jc1oqp70m94732fh.apps.googleusercontent.com'
CLIENT_SECRET = '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'
REFRESH_TOKEN = '1//05jYy_Ale00w3CgYIARAAGAUSNwF-L9IrSWrGSS3R5qTJ33Z-YIc8eHOvVNPV809albtGNvI7swxk8D8ekaN0yXsHmfm9QQlayUU'

def get_access_token():
    data = urllib.parse.urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
        'grant_type': 'refresh_token'
    }).encode()
    req = urllib.request.Request(
        'https://oauth2.googleapis.com/token',
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    if 'access_token' not in result:
        raise Exception(f"Token error: {result}")
    return result['access_token']

def gmail_get(access_token, path):
    url = f'https://gmail.googleapis.com/gmail/v1/users/me/{path}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {access_token}'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def get_body(payload):
    """Recursively extract plain text body."""
    if payload.get('body', {}).get('data'):
        return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='replace')
    parts = payload.get('parts', [])
    for part in parts:
        if part.get('mimeType') == 'text/plain':
            data = part.get('body', {}).get('data', '')
            if data:
                return base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')
    for part in parts:
        result = get_body(part)
        if result:
            return result
    return ''

def main():
    print("Getting access token...")
    token = get_access_token()
    print(f"Token OK: {token[:20]}...")

    # Search for recent emails from Travis or Vanessa
    query = 'from:(travis@excel-plumbing.com OR vanessa@excel-plumbing.com)'
    encoded = urllib.parse.urlencode({'q': query, 'maxResults': '10'})
    search = gmail_get(token, f'messages?{encoded}')
    
    messages = search.get('messages', [])
    print(f"Found {len(messages)} emails from Travis/Vanessa")
    
    if not messages:
        print("NO_EMAILS_FOUND")
        return
    
    # Check each message for Slack credentials
    for msg_info in messages:
        msg_id = msg_info['id']
        msg = gmail_get(token, f'messages/{msg_id}?format=full')
        
        headers = {h['name']: h['value'] for h in msg.get('payload', {}).get('headers', [])}
        subject = headers.get('Subject', '(no subject)')
        from_addr = headers.get('From', '(unknown)')
        date = headers.get('Date', '(unknown)')
        body = get_body(msg.get('payload', {}))
        
        print(f"\nMessage ID: {msg_id}")
        print(f"From: {from_addr}")
        print(f"Date: {date}")
        print(f"Subject: {subject}")
        
        # Check for Slack bot token
        bot_token_match = re.search(r'xoxb-[A-Za-z0-9\-]+', body)
        signing_secret_match = re.search(r'[0-9a-f]{32}', body)
        workspace_match = re.search(r'https://[a-zA-Z0-9\-]+\.slack\.com', body)
        channel_match = re.search(r'#[a-zA-Z0-9\-_]+', body)
        
        if bot_token_match:
            print(f"*** SLACK BOT TOKEN FOUND: {bot_token_match.group()}")
            print(f"Body:\n{body[:2000]}")
            if signing_secret_match:
                print(f"Potential signing secret: {signing_secret_match.group()}")
            if workspace_match:
                print(f"Workspace URL: {workspace_match.group()}")
            if channel_match:
                print(f"Channel: {channel_match.group()}")
        else:
            print(f"Body preview: {body[:300]}")

if __name__ == '__main__':
    main()
