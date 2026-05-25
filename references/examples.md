# Jira Examples

## Example 1: "Create a bug for the payment crash"
```
search_issues(jql: "summary ~ 'payment crash'") → [] (no duplicate)
create_issue(project: "PROJ", type: "Bug", summary: "fix: payment service crashes on empty cart", description: "## Steps\n1. Add nothing to cart\n2. Click pay\n## Expected: Error message\n## Actual: 500 crash", priority: "Critical")
```
Response: "✅ PROJ-131 created (Critical bug). Assigned to @payments-team."

## Example 2: "Plan next sprint"
```
get_board(id: "board_1") → {velocity: 34 points}
search_issues(jql: "sprint is EMPTY AND status = 'To Do' ORDER BY priority") → 12 issues, 52 points total
→ Recommend: take top 8 issues (34 points) to match velocity
add_to_sprint(sprint_id: "sprint_15", issues: ["PROJ-125", ...])
```
Response: "Sprint 15 planned: 8 issues, 34 points (matches team velocity)."

## Example 3: "What's blocking the release?"
```
search_issues(jql: "fixVersion = 'v2.4' AND status != Done") → [{key: "PROJ-128", status: "In Review"}, {key: "PROJ-129", status: "Blocked"}]
get_issue(key: "PROJ-129") → {blocker: "Waiting on API spec from partner"}
```
Response: "2 issues blocking v2.4:\n- PROJ-128: In Review (needs reviewer)\n- PROJ-129: Blocked (waiting on partner API spec)"
