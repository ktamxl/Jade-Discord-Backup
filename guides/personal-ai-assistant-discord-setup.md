# 🤖 How to Set Up Your Own Private Personal AI Assistant on Discord

**Written by Sisi 🌸 | For Excel MaxClaw Team Members**

This guide walks you through creating your own private personal AI assistant — just like Ken's "Sisi Personal Bot" — powered by MaxClaw. Your assistant will only talk to you, live in Discord, and be completely separate from the team workspace.

---

## What You'll End Up With

- Your own private AI assistant bot on Discord
- Only you can talk to it — completely private
- Runs 24/7 on MaxClaw's platform
- You can customize its name, personality, and capabilities

---

## Overview of Steps

1. Sign up for MaxClaw (your own personal workspace)
2. Create a Discord bot in the Developer Portal
3. Connect the bot to your MaxClaw workspace
4. Pair your Discord account
5. Tell Sisi MaxClaw to finalize the server setup
6. Start chatting!

---

## Step 1 — Sign Up for MaxClaw

1. Go to **[maxclaw.ai](https://maxclaw.ai)** (or wherever your team's MaxClaw access is provided)
2. Create your own **personal workspace** — this is separate from the Excel team workspace
3. Once set up, you'll have your own AI agent to configure

> 💡 The Excel team workspace (Sisi MaxClaw) is shared. Your personal workspace is yours alone.

---

## Step 2 — Create Your Discord Bot

### 2a. Go to the Discord Developer Portal
- Visit: **[discord.com/developers/applications](https://discord.com/developers/applications)**
- Click **"New Application"**
- Name it something personal, e.g. **"[YourName] Personal Bot"**
- Click **"Create"**

### 2b. Set Up the Bot
- Click **"Bot"** in the left sidebar
- Scroll down to **"Privileged Gateway Intents"** and enable:
  - ✅ **Message Content Intent** ← Required
  - ✅ **Server Members Intent** ← Recommended
  - ⬜ Presence Intent ← Skip this one
- Click **"Save Changes"**

### 2c. Get Your Bot Token
- Scroll up on the Bot page
- Click **"Reset Token"** → confirm → **copy the token immediately**
- ⚠️ Save it somewhere safe — it's only shown once!

### 2d. Generate an Invite Link & Add Bot to Server
- Click **"OAuth2"** in the left sidebar
- Under **"OAuth2 URL Generator"**, check:
  - ✅ `bot`
  - ✅ `applications.commands`
- Under **"Bot Permissions"**, check:
  - ✅ View Channels
  - ✅ Send Messages
  - ✅ Read Message History
  - ✅ Embed Links
  - ✅ Attach Files
- Copy the generated URL → paste it in your browser
- Select the **Excel MaxClaw server** (or your own server) → click **Authorize**

---

## Step 3 — Connect Discord to Your MaxClaw Workspace

In your MaxClaw personal workspace, tell your agent:

> *"I want to set up Discord. Here is my bot token: [paste token here]. Please configure it for me."*

Your agent will handle the config automatically — no technical knowledge needed.

---

## Step 4 — Enable Discord DMs from Server Members

This one-time setting lets you DM your bot:

1. Open Discord → go to the shared server where your bot is
2. **Right-click the server icon** → **Privacy Settings**
3. Toggle ON: **"Direct Messages"** ✅

---

## Step 5 — Pair Your Discord Account

1. Find your bot in the server's member list
2. Click its name → **"Message"** → send any message (e.g. "hi")
3. The bot will reply with a **pairing code** like: `PAIR-XXXXXXXX`
4. Copy that code and send it to your MaxClaw agent:
   > *"Approve this Discord pairing code: PAIR-XXXXXXXX"*
5. Your agent approves it — you're connected! 🎉

---

## Step 6 — Tell Sisi MaxClaw to Finalize the Server Setup

Once your personal bot is in the server and paired, message **Sisi MaxClaw** in the Excel MaxClaw team channel with the following:

> *"Hi Sisi MaxClaw! I've just set up my personal bot [YourName Personal Bot]. Can you please:*
> *1. Ban my personal bot from the #sisi-maxclaw channel (so it doesn't interfere with team conversations)*
> *2. Give my personal bot the Administrator role so it has full control over my personal channel*
> *3. Add a channel link to #[your-personal-channel] in the Personal Agent section of the server"*

Sisi MaxClaw will take care of all three steps automatically — no manual Discord settings needed on your end.

---

## Step 7 — Start Chatting!

You can now DM your personal bot on Discord anytime. It's your private AI assistant — the team has no access to your conversations.

**Try saying:**
- "What can you do?"
- "Help me draft an email"
- "Search the web for..."
- "Remind me about our next team meeting"

---

## Privacy & Security Notes

- 🔒 **Only you can interact** with your bot — it's locked to your Discord user ID
- 🔒 **Your conversations are private** — not visible to the team or Sisi MaxClaw
- 🔒 **Your bot token is secret** — never share it with anyone
- 🔒 **If your token leaks**, go to the Developer Portal → Bot → Reset Token immediately

---

## Customizing Your Assistant

Once connected, you can ask your agent to:
- Give itself a **name and personality**
- Set up **reminders and cron jobs**
- Connect to **your email, calendar**, or other tools
- Learn your **preferences and working style**

---

## Need Help?

Ask **Sisi MaxClaw** in the Excel team Discord — she can relay setup instructions and help troubleshoot. She can't access your personal workspace, but she can guide you through the process.

---

*Guide prepared by Sisi 🌸 | Ken Tam's Personal AI Assistant*
*Last updated: March 2026*
