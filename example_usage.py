"""Example usage for Software UI Clickpath Planner."""
from client import SoftwareUIClickpathPlanner

if __name__ == "__main__":
    plan = SoftwareUIClickpathPlanner.plan_workflow("Invite engineer to workspace", "https://cloud.console.io")
    print("Steps planned:", plan["total_steps"])
    for s in plan["execution_plan"]:
        print("->", s["action"], s.get("target", ""))
