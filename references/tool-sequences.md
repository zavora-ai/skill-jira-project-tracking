# Jira Tool Sequences

## Tools (15)
| Tool | Purpose |
|------|---------|
| `list_projects` | All projects |
| `get_project` | Project details |
| `search_issues` | JQL search |
| `get_issue` | Full issue details |
| `create_issue` | Create story/bug/task |
| `update_issue` | Update fields |
| `transition_issue` | Move through workflow |
| `assign_issue` | Assign to user |
| `add_comment` | Add comment |
| `list_comments` | Issue comments |
| `get_transitions` | Valid next states |
| `list_sprints` | Sprints for board |
| `create_sprint` | New sprint |
| `add_to_sprint` | Move issues to sprint |
| `get_board` | Board config + velocity |

## Sequence: Create Well-Structured Issue (2 calls)
```
1. search_issues(jql: "summary ~ 'similar'") → check duplicates
2. create_issue(project: "PROJ", type: "Story", summary: "...", description: "## AC\n- [ ] ...", priority: "High", labels: ["payments"])
```

## Sequence: Sprint Planning (3 calls)
```
1. get_board(id) → {velocity_avg: 34}
2. search_issues(jql: "project = PROJ AND sprint is EMPTY AND status = 'To Do' ORDER BY priority DESC")
3. add_to_sprint(sprint_id, issues: top N by velocity)
```

## Sequence: Transition with Context (3 calls)
```
1. get_issue(key: "PROJ-123") → current status
2. get_transitions(key: "PROJ-123") → valid moves
3. transition_issue(key: "PROJ-123", transition_id: "31") + add_comment("Moving to Done: all AC met")
```
