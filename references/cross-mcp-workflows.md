# Jira Cross-MCP Workflows

## Jira + GitHub: PR → Issue Linking
```
GITHUB: merge_pull_request(title: "fix: PROJ-123 null pointer")
JIRA: transition_issue(key: "PROJ-123", to: "Done")
JIRA: add_comment(key: "PROJ-123", body: "Fixed in PR #42, merged to main")
```

## Jira + Slack: Sprint Notifications
```
JIRA: create_sprint(name: "Sprint 14", goal: "Ship payment retry")
JIRA: add_to_sprint(sprint_id, issues: [...])
SLACK: send_message(channel: "#team", text: "🏃 Sprint 14 started\nGoal: Ship payment retry\n8 stories, 3 bugs")
```

## Jira + CI/CD: Build Failure → Bug
```
CICD: get_pipeline_logs(run_id) → "test_payment_retry failed"
JIRA: create_issue(type: "Bug", summary: "fix: payment retry test failing on main", priority: "High")
JIRA: assign_issue(key: "PROJ-130", assignee: "last_committer")
```
