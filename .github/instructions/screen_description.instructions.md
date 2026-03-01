---
applyTo: '**'
---

# Screen Description Generation Instructions

## Input
- HTML mockup file (low-fidelity wireframe)
- Use case description and functional requirements

## Output Format
Generate a simple screen description document with only the Screen Elements section in markdown table format:

```markdown
# UC-[ID]: [Use Case Name] - Screen Description

## Screen Elements

| Field Name | Description |
|------------|-------------|
| **[Field/Element Name in Vietnamese]** | [Type]: [Data type, constraints, behavior, validation rules, etc.] |
```

## Guidelines
- List all visible screen elements
- Include input fields, buttons, labels, and display elements
- Specify data types, constraints, and validation rules
- Document required vs optional fields
- Describe button actions and behaviors
- Note any error messages or notifications
- Keep the output simple - only include the title and Screen Elements table
- Do not add additional sections like Validation Rules, Business Rules, or Post-Submission Behavior
 - Field names: Display each Field Name in Vietnamese. If helpful, include the English term in parentheses after the Vietnamese label (example: **Tên lớp (Class Name)**).

