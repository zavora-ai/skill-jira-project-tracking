#!/usr/bin/env python3
"""
Sprint Capacity Calculator
Recommends sprint scope based on historical velocity.
Usage: python sprint_capacity.py '{"velocity_history": [32, 36, 34], "backlog": [{"key": "PROJ-125", "points": 8}, ...]}'
"""
import json
import sys


def calculate(data):
    history = data.get("velocity_history", [])
    backlog = data.get("backlog", [])
    buffer_pct = data.get("buffer_pct", 10)  # 10% buffer by default

    if not history:
        return {"error": "Need at least 1 sprint of velocity history"}

    avg_velocity = sum(history) / len(history)
    target = int(avg_velocity * (1 - buffer_pct / 100))

    # Select items that fit
    selected = []
    total_points = 0
    for item in backlog:
        pts = item.get("points", 0)
        if total_points + pts <= target:
            selected.append(item)
            total_points += pts

    overflow = sum(i.get("points", 0) for i in backlog) - total_points

    return {
        "avg_velocity": round(avg_velocity, 1),
        "target_points": target,
        "buffer_pct": buffer_pct,
        "selected_count": len(selected),
        "selected_points": total_points,
        "selected_items": [i.get("key", "") for i in selected],
        "overflow_points": overflow,
        "recommendation": f"Take {len(selected)} items ({total_points} pts). Velocity avg: {avg_velocity:.0f}. Leave {overflow} pts for next sprint.",
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python sprint_capacity.py \'{"velocity_history": [32, 36, 34], "backlog": [...]}\'')
        sys.exit(1)
    print(json.dumps(calculate(json.loads(sys.argv[1])), indent=2))
