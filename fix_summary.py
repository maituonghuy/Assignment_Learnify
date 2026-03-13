import csv

efforts = {"Nghĩa": {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0},
           "ToanDV": {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0},
           "HuyMT": {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0},
           "AnhNHH": {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0},
           "DuongNC": {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0}}

with open("WSB.csv", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split(",")
        try:
            # First row or View Homepage
            if "Simple" not in parts and "Medium" not in parts and "Complex" not in parts:
                continue
            
            # Find effort
            effort = 0
            iteration = ""
            assignee = ""
            for i, p in enumerate(parts):
                if p.isdigit():
                    effort = int(p)
                if p.startswith("Iteration "):
                    iteration = p
                if p in efforts:
                    assignee = p
            
            if assignee and iteration and effort > 0:
                efforts[assignee][iteration] += effort
                efforts[assignee]["Total"] += effort
        except Exception as e:
            print(f"Error {e} on line {line}")

output_table = "| Member | Iteration 1 | Iteration 2 | Iteration 3 | Total |\n|--------|-------------|-------------|-------------|-------|\n"

total_i1 = total_i2 = total_i3 = total_sum = 0
for member in ["Nghĩa", "ToanDV", "HuyMT", "AnhNHH", "DuongNC"]:
    i1 = efforts[member].get("Iteration 1", 0)
    i2 = efforts[member].get("Iteration 2", 0)
    i3 = efforts[member].get("Iteration 3", 0)
    tot = efforts[member].get("Total", 0)
    output_table += f"| {member} | {i1} | {i2} | {i3} | {tot} |\n"
    total_i1 += i1
    total_i2 += i2
    total_i3 += i3
    total_sum += tot

output_table += f"| **Total** | **{total_i1}** | **{total_i2}** | **{total_i3}** | **{total_sum}** |"

print(output_table)

import re
with open("function_assignment.md", "r", encoding="utf-8") as f:
    text = f.read()

new_text = re.sub(r"## Summary - Effort per Person per Iteration\n\n\| Member.*?(?=\n\n|\Z)", "## Summary - Effort per Person per Iteration\n\n" + output_table, text, flags=re.DOTALL)

with open("function_assignment.md", "w", encoding="utf-8") as f:
    f.write(new_text)

