## [LRN-20260315-001] platform_behavior

**Logged**: 2026-03-15T21:40:00+08:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
Telegram streaming: "partial" setting causes duplicate/partial message display on long replies

### Details
Ken reported seeing long replies sent twice on Telegram — first partial, then the full message restarts from the beginning. This is caused by the "streaming: partial" channel setting. The message is streamed chunk by chunk, and Telegram users see earlier chunks re-appear as the full message is finalized.

### Suggested Action
Change channels.telegram.streaming from "partial" to "off" (wait until full reply is ready, then send once) using safe_config_update.mjs. This eliminates the visual duplication for the user.

### Metadata
- Source: user_feedback
- Related Files: /root/.openclaw/openclaw.json
- Tags: telegram, streaming, duplication, ux
- Pattern-Key: telegram.streaming.partial.duplication
- Recurrence-Count: 1
- First-Seen: 2026-03-15

---

## [LRN-20260325-001] knowledge_gap

**Logged**: 2026-03-25T07:12:00+08:00
**Priority**: medium
**Status**: pending
**Area**: config

### Summary
WeChat integration in MaxClaw is WeCom (企業微信/WeChat Work) only — not personal WeChat accounts. ClawBot is a separate Tencent-side product.

### Details
When Ken asked about WeChat setup, initial research suggested "personal WeChat" support was announced. However, the actual installed plugin is `wecom-openclaw-plugin` which requires WeCom Bot ID + Secret from an enterprise WeCom organization — NOT a personal WeChat QR code scan. ClawBot (announced March 22) is a Tencent-side plugin that wraps OpenClaw, but it is NOT configurable via MaxClaw settings. These are two separate things:
1. **WeCom plugin** (installed): Enterprise WeChat Work bot — requires WeCom org + Bot ID + Secret
2. **ClawBot** (Tencent product): Personal WeChat → OpenClaw integration — configured in WeChat app, not MaxClaw config

### Suggested Action
Before advising users on WeChat setup, clarify which type they need: personal WeChat (ClawBot path) vs. WeCom enterprise (WeCom plugin path). Do NOT conflate them.

### Metadata
- Source: conversation
- Related Files: /app/openclaw/extensions/wecom-openclaw-plugin/README.md
- Tags: wechat, wecom, clawbot, channels

---
