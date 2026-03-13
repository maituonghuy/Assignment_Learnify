import csv
import re

# Updates for WSB.csv
# Structure seems to be: 
# Function, Type(maybe), Feature, Sub Feature, Description, Level, Effort, Iteration, Status, Assignee, Priority

# Function mapping: (New Assignee, New Iteration)
updates = {
    "Update Question In Resource Bank": ("Nghĩa", "Iteration 2"),
    "Delete Question In Resource Bank": ("Nghĩa", "Iteration 2"),
    "Download Resource Bank": ("Nghĩa", "Iteration 2"),
    "Create Assignment Manual": ("Nghĩa", "Iteration 2"),
    "Update Assignment": ("Nghĩa", "Iteration 2"),
    "Create Question By Importing Files": ("Nghĩa", "Iteration 2"),
    "Create Assignment By Importing From Resource Bank": ("Nghĩa", "Iteration 2"),
    "Create Assignment By Uploading Files": ("Nghĩa", "Iteration 2"),
    "Delete Assignment": ("Nghĩa", "Iteration 2"),
    "Remove Student": ("ToanDV", None),
    "Update User Status": ("ToanDV", None)
}

lines = []
with open("WSB.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split(",")
        # Check if first part matches or if it's the weird View Homepage line
        func_name = parts[0]
        # if func_name == "Authentication & User Profile":
        # It's that weird line, skip updating it
        if func_name in updates:
            new_assignee, new_iter = updates[func_name]
            # Replace Assignee and Iteration
            # The structure is Function,Type,Feature,Sub Feature,Desc,Level,Effort,Iteration,Status,Assignee,Priority
            # Let's find index. 'Status' is usually 'Planned', 'Effort' is numeric.
            planned_idx = -1
            assignee_idx = -1
            for i, p in enumerate(parts):
                if p.startswith("Iteration "):
                    planned_idx = i
                if p in ["Nghĩa", "ToanDV", "HuyMT", "AnhNHH", "DuongNC"]:
                    assignee_idx = i
                    
            if assignee_idx != -1:
                parts[assignee_idx] = new_assignee
            if new_iter and planned_idx != -1:
                parts[planned_idx] = new_iter
        lines.append(",".join(parts))

with open("WSB.csv", "w", encoding="utf-8") as f:
    for l in lines:
        f.write(l + "\n")

print("WSB.csv updated successfully")
