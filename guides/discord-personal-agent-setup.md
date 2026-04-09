# 🌸 Personal Agent Discord Channel Setup Guide
*Prepared by Jade for Sisi MaxClaw & the Excel team*
*Version 1.0 — March 2026*

---

## Overview

This guide walks through setting up a **private Discord channel** for each team member's personal AI agent, including:
- Creating a private channel just for you and your agent
- Configuring the agent to respond in that channel
- Setting up the agent's name and avatar
- Creating your own avatar illustration

---

## Step 1: Create a Private Discord Channel

1. In your Discord server, click the **+** icon next to **Text Channels**
2. Name it something like `#jade-ken-personal` or `#sisi-vanessa` (agent name first, then yours)
3. Set it to **Private Channel** ✅
4. Invite only yourself (and the agent bot if it's not already in the server)
5. Optional: Set a channel topic (e.g. "Private channel for Ken & Jade 🌸")

---

## Step 2: Configure the Agent to Respond in That Channel

Ask your agent (Sisi) to patch the Discord config to allow your new channel. Give her:
- Your **Guild ID** (Server ID) — right-click your server name → Copy Server ID
- Your **Channel ID** — right-click your new channel → Copy Channel ID
- Your **User ID** — right-click your username → Copy User ID

Then tell Sisi:
> "Please add my channel [CHANNEL_ID] to the Discord allowlist in the config, and make sure my user ID [USER_ID] is included."

Sisi will use `config.patch` to add the channel under:
```
channels.discord.guilds.[GUILD_ID].channels.[CHANNEL_ID]: { allow: true }
```

And add your user ID to the `users` array.

---

## Step 3: Test It

Send a message in your new private channel. Your agent should respond within a few seconds.

If no response:
- Make sure the bot has access to the channel (check channel permissions in Discord)
- Ask Sisi to verify the config was saved correctly

---

## Step 4: Rename Your Agent (Optional)

If your personal agent shares a name with another team agent, you can rename yours. Ask your agent:
> "I'd like to rename you. What name would you like, and what does it take?"

The agent can:
1. Update its own identity files (`IDENTITY.md`, `MEMORY.md`)
2. Change the Discord bot username via API (if it's a separate bot)
3. Update the MaxClaw dashboard name via `ui.assistant.name` in the config

---

## Step 5: Set the Agent's Avatar in Discord

1. Go to the **Discord Developer Portal**: <https://discord.com/developers/applications>
2. Click on your agent's app (e.g. "Jade Personal Bot")
3. Under **General Information** → click the app icon/avatar
4. Upload your chosen avatar image
5. Click **Save Changes**

The avatar will now show next to every message your agent sends in Discord.

To **generate an avatar** for your agent, ask them:
> "Can you generate an illustrated portrait avatar for yourself? I'd like [elegant/cute/professional] style."

The agent will generate options using AI image tools and let you pick one.

---

## Step 6: Create Your Own Avatar (Optional but Fun!)

You can also create an illustrated avatar for yourself! Send your agent a photo and say:
> "Can you turn this into an anime/illustrated style avatar for me? Keep my natural eye color."

⚠️ **Important note:** AI image tools sometimes change Asian eyes to blue — always specify:
> "Keep natural dark brown eyes. Do not change eye color."

Your agent will generate the illustrated version and save it to the workspace for you to use anywhere.

---

## Step 7: Update the Channel Name If Needed

After everything is set up, you can rename the Discord channel to match (e.g. `#jade-ken-personal`). Right-click the channel → **Edit Channel** → change the name.

---

## Summary Checklist

- [ ] Private Discord channel created
- [ ] Channel ID added to agent config (`config.patch`)
- [ ] Agent responds in the channel ✅
- [ ] Agent renamed (if needed)
- [ ] Agent avatar set in Discord Developer Portal
- [ ] Your own avatar created (optional)
- [ ] Channel name updated (optional)

---

## Quick Reference — What to Ask Your Agent

| Task | What to say |
|------|-------------|
| Add channel to config | "Add channel [ID] to my Discord allowlist" |
| Rename agent | "Let's talk about changing your name" |
| Generate agent avatar | "Generate an illustrated portrait avatar for yourself" |
| Generate my avatar | "Turn this photo into an anime avatar — keep dark brown eyes" |
| Check context usage | "/status" |
| Save something to memory | "Remember this: [info]" |

---

*Prepared by Jade 💚 — Personal Assistant to Ken Tam*
*For questions, ask Jade or Sisi MaxClaw*
