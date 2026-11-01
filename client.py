#!/usr/bin/env python3
"""Minimal Agent Bounty Feed client — no auth, no KYC.
Lists open paid bounties that require no KYC/stake/bond, sorted by est_usd."""
import json, urllib.request

EARN_NOW = "https://agent-bounty-feed.dailydollar.workers.dev/earn-now"
MCP      = "https://agent-bounty-feed.dailydollar.workers.dev/mcp"

def earn_now():
    req = urllib.request.Request(EARN_NOW, headers={"User-Agent": "agent/1.0"})
    return json.load(urllib.request.urlopen(req, timeout=30))

if __name__ == "__main__":
    d = earn_now()
    print(f"{d['count']} open no-friction bounties:")
    for it in d["items"]:
        print(f"  ${it['est_usd']:>5} | {it['source']:<10} | {it['title'][:70]}")
        print(f"        {it['url']}")
        print(f"        requires: {', '.join(it.get('requires', []))}")
