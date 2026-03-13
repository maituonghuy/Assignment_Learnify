import re

with open("function_assignment.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. ToanDV to Nghĩa
text = text.replace("""### Question Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|----------|
| Update Question In Resource Bank | 5 | Medium |
| Delete Question In Resource Bank | 2 | Low |
| Download Resource Bank | 5 | Medium |

""", "")

text = text.replace("""### Assignment Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|----------|
| Create Assignment Manual | 7 | Highest |
| Update Assignment | 5 | High |

""", "")

# 2. AnhNHH to Nghĩa
text = text.replace("""### Question Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|----------|
| Create Question By Importing Files | 7 | High |

""", "")

text = text.replace("""### Assignment Management (Iteration 3)
| Function | Effort | Priority |
|----------|--------|----------|
| Create Assignment By Importing From Resource Bank | 5 | High |
| Create Assignment By Uploading Files | 7 | Highest |
| Delete Assignment | 2 | Low |

""", "")

# 3. HuyMT to ToanDV
text = text.replace("""### User & System Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|---------|
| Remove Student | 2 | Low |
| Update User Status | 5 | Medium |
| View System Dashboard | 5 | Medium |""", """### User & System Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|---------|
| View System Dashboard | 5 | Medium |""")

text = text.replace("""### User & System Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|---------|
| View Student Information | 2 | Medium |
| View User List | 3 | High |""", """### User & System Management (Iteration 2)
| Function | Effort | Priority |
|----------|--------|---------|
| View Student Information | 2 | Medium |
| View User List | 3 | High |
| Remove Student | 2 | Low |
| Update User Status | 5 | Medium |""")

# Add to Nghia Question Management
text = text.replace("""### Question Management (Iteration 1 & 2)
| Function | Effort | Iteration | Priority |
|----------|--------|-----------|----------|
| Create Question Manual | 5 | Iter 1 | High |
| Create Question With AI | 10 | Iter 2 | High |""", """### Question Management (Iteration 1 & 2)
| Function | Effort | Iteration | Priority |
|----------|--------|-----------|----------|
| Create Question Manual | 5 | Iter 1 | High |
| Create Question With AI | 10 | Iter 2 | High |
| Update Question In Resource Bank | 5 | Iter 2 | Medium |
| Delete Question In Resource Bank | 2 | Iter 2 | Low |
| Download Resource Bank | 5 | Iter 2 | Medium |
| Create Question By Importing Files | 7 | Iter 2 | High |""")

# Add to Nghia Assignment Management
text = text.replace("""### Assignment Management (Iteration 3)
| Function | Effort | Priority |
|----------|--------|----------|
| View Assignment (Student) | 2 | High |
| View Assignment (Teacher) | 2 | Medium |
| Create Assignment With AI | 7 | Highest |""", """### Assignment Management (Iteration 2 & 3)
| Function | Effort | Iteration | Priority |
|----------|--------|-----------|----------|
| Create Assignment Manual | 7 | Iter 2 | Highest |
| Update Assignment | 5 | Iter 2 | High |
| Create Assignment By Importing From Resource Bank | 5 | Iter 2 | High |
| Create Assignment By Uploading Files | 7 | Iter 2 | Highest |
| Delete Assignment | 2 | Iter 2 | Low |
| View Assignment (Student) | 2 | Iter 3 | High |
| View Assignment (Teacher) | 2 | Iter 3 | Medium |
| Create Assignment With AI | 7 | Iter 3 | Highest |""")

with open("function_assignment.md", "w", encoding="utf-8") as f:
    f.write(text)
