"""MCP server for Software UI Clickpath Planner."""
import sys
import json
from client import SoftwareUIClickpathPlanner

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "plan_ui_clickpath",
                "description": "Plans step-by-step UI automation macro for a given software goal",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "goal": {"type": "string"},
                        "target_platform": {"type": "string"}
                    },
                    "required": ["goal", "target_platform"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "plan_ui_clickpath":
            args = params.get("arguments", {})
            res = SoftwareUIClickpathPlanner.plan_workflow(args.get("goal", ""), args.get("target_platform", ""))
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
