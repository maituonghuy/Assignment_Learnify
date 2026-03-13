import re

with open("function_assignment.md", "r", encoding="utf-8") as f:
    text = f.read()

# Let's extract the tables automatically to calculate the points
from collections import defaultdict
efforts = defaultdict(lambda: {"Iteration 1": 0, "Iteration 2": 0, "Iteration 3": 0, "Total": 0})

current_member = None
current_iteration = None

for line in text.split("\n"):
    m = re.match(r"^## ([A-Za-z]+)", line)
    if m and m.group(1) != "Summary":
        current_member = m.group(1)
    
    m2 = re.match(r"^### .*?\(Iteration (.*?)\)", line)
    if m2:
        iters = m2.group(1).replace(" & ", ", ").split(", ")
        current_iteration = ["Iteration " + i.strip() for i in iters]

    # matches table row | Name | Effort | [Iteration] | Priority |
    if line.startswith("|") and not line.startswith("| Function") and not line.startswith("|---") and not line.startswith("| Member"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 2:
            try:
                effort = int(parts[1])
                # determine iteration
                if len(parts) == 4 and "Iter" in parts[2]:
                    # Format: | Name | Effort | Iteration | Priority |
                    iter_val = parts[2].replace("Iter", "Iteration")
                    efforts[current_member][iter_val] += effort
                    efforts[current_member]["Total"] += effort
                else:
                    # use current_iteration
                    if current_iteration:
                        if len(current_iteration) == 1:
                            efforts[current_member][current_iteration[0]] += effort
                            efforts[current_member]["Total"] += effort
                        else:
                            pass # shouldn't happen without the Iteration column unless messed up
            except:
                pass

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

new_text = re.sub(r"## Summary - Effort per Person per Iteration\n\n\| Member.*?(?=\n\n|\Z)", "## Summary - Effort per Person per Iteration\n\n" + output_table, text, flags=re.DOTALL)

with open("function_assignment.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print(output_table)
