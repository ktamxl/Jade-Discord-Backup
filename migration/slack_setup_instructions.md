# Slack Setup — What to Do When Credentials Arrive

## Context
- Sisi emailed Travis + Vanessa on 2026-03-18 from payables@excel-plumbing.com
- They will reply TO payables@excel-plumbing.com with Slack credentials
- Ken is NOT involved — Travis/Vanessa deal directly with Sisi

## When email arrives with credentials, extract:
1. Bot Token (xoxb-...)
2. Signing Secret (from Basic Information > App Credentials)
3. Slack workspace URL (e.g. excelplumbing.slack.com)
4. Channel name (e.g. #sisi or #ai-assistant)

## Config to patch into OpenClaw (channels.slack):
```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "botToken": "xoxb-REPLACE",
      "signingSecret": "REPLACE",
      "mode": "http"
    }
  }
}
```
Note: Use HTTP mode (not socket mode) since we don't have app token.
Socket mode requires xapp- token. HTTP mode only needs botToken + signingSecret.

## After configuring:
1. Restart gateway (ask Ken to restart via MaxClaw settings)
2. Send test message from Slack to Ken
3. Update /workspace/memory/excel_plumbing.md with Slack status
4. Update /workspace/memory/slack_setup.md with completion note

## Gmail OAuth creds: /workspace/memory/gmail_oauth_credentials.md
