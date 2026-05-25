# Jira Project Tracking Skill

> Agile project management for AI agents — JQL search, sprint planning, issue lifecycle, velocity tracking, and cross-system coordination across GitHub and Slack.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--jira-green)](https://github.com/zavora-ai/mcp-jira)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 15 Jira tools into **disciplined agile workflows** — ensuring issues are well-structured, sprints are capacity-aware, and status changes are always documented.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Create Issue | 2 | Duplicate check + structured creation with AC |
| Search Issues | 1 | JQL-powered queries for any filter |
| Sprint Management | 3-4 | Velocity-aware planning + scope tracking |
| Transition Issue | 3 | Valid state check + move + comment |
| Board Overview | 2 | Current sprint status at a glance |

### Without this skill:
- Issues created without acceptance criteria or labels
- Sprints overloaded beyond team velocity
- Status changes without context (why was this moved?)
- No duplicate checking before creating
- No cross-system linking (PRs, Slack)

### With this skill:
- Every issue has type, priority, acceptance criteria, and labels
- Sprint scope matched to team velocity (last 3 sprints avg)
- Every transition documented with reason
- Duplicate detection before creation
- Auto-links to GitHub PRs and Slack notifications

## Installation

### Claude Code
```bash
git clone https://github.com/zavora-ai/skill-jira-project-tracking.git \
  ~/.skills/skills/jira-project-tracking
```

### ADK-Rust
```bash
cp -r jira-project-tracking /path/to/project/.skills/skills/
```

### Claude.ai
Download ZIP → Settings > Capabilities > Skills > Upload

## Requirements

**Required:**
- `mcp-jira` server connected (15 tools)

**Cross-MCP integrations:**
- `mcp-github` — PR merged → auto-transition issue to Done
- `mcp-slack` — Sprint start/end notifications to team channel

## Folder Structure

```
jira-project-tracking/
├── SKILL.md                       # Decision tree + 5 workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── sprint_capacity.py         # Velocity-based sprint capacity calculator
├── assets/
│   └── sprint-report.md           # Sprint review output template
├── references/
│   ├── tool-sequences.md          # 15 tools + JQL patterns + transition map
│   ├── cross-mcp-workflows.md     # Jira + GitHub + Slack orchestration
│   └── examples.md                # 3 real scenarios with full traces
├── README.md
└── LICENSE
```

## How It Works

### Decision Tree

```
User request arrives
├── "create ticket", "new issue", "bug"? → Create Issue (with duplicate check)
├── "search", "find", "JQL"? → Search Issues
├── "sprint", "plan", "velocity"? → Sprint Management
├── "move", "transition", "done"? → Transition Issue
└── "board", "status"? → Board Overview
```

### Sprint Planning (Velocity-Aware)

The skill checks team velocity before committing sprint scope:
1. Gets average velocity from last 3 sprints
2. Searches prioritized backlog
3. Recommends scope that fits capacity
4. Flags if requested scope exceeds velocity

## Example

**User:** "Plan next sprint for the payments team"

**Agent behavior:**
1. Gets board velocity (avg 34 points/sprint)
2. Searches backlog sorted by priority
3. Selects top items fitting 34 points
4. Creates sprint and adds issues

**Result:**
```
✅ Sprint 15 planned

Goal: Ship payment retry logic
Items: 8 stories (34 points) — matches team velocity
Top items:
- PROJ-125: Payment retry with backoff (8 pts)
- PROJ-126: Webhook timeout handling (5 pts)
- PROJ-127: Idempotency keys (5 pts)
...
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on Jira/project queries |
| Issue quality | All issues have type + priority + acceptance criteria |
| Sprint discipline | Scope matches velocity, mid-sprint changes flagged |
| Transition docs | Every status change has a comment explaining why |

## Scripts

### `sprint_capacity.py`
Calculates recommended sprint scope based on historical velocity:
```bash
python scripts/sprint_capacity.py '{"velocity_history": [32, 36, 34], "backlog_points": 52}'
# → {"recommended_points": 34, "can_fit": 8, "overflow": 18}
```

## MCP Server Compatibility

Designed for [mcp-jira](https://github.com/zavora-ai/mcp-jira):

| Capability | Tools |
|-----------|-------|
| Projects | list_projects, get_project |
| Issues | search_issues, get_issue, create_issue, update_issue |
| Workflow | transition_issue, assign_issue, get_transitions |
| Comments | add_comment, list_comments |
| Sprints | list_sprints, create_sprint, add_to_sprint |
| Boards | get_board |

## Related Skills

- [skill-github-development](https://github.com/zavora-ai/skill-github-development) — PR → issue linking
- [skill-slack-collaboration](https://github.com/zavora-ai/skill-slack-collaboration) — Sprint notifications

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
