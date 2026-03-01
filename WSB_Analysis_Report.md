# Learnify - Work Breakdown Structure (WSB) Analysis Report

> **Project:** Learnify - Online Classroom Management Platform
> **Date:** February 2026
> **Team Size:** 5 members
> **Total Iterations:** 3 (each ~2 weeks)
> **Total Functions:** 81
> **Total Estimated Effort:** 147 person-days

---

## 1. Executive Summary

This WSB decomposes the Learnify platform into **81 functional screens/functions** across **6 feature areas**, 
with a total estimated effort of **147 person-days**. The work is distributed across 3 iterations:

- **Iteration 1:** 36 functions, 50 person-days
- **Iteration 2:** 24 functions, 50 person-days
- **Iteration 3:** 21 functions, 47 person-days

**Team Capacity:** 5 members × 2 weeks/iteration × 6 working days = **60 person-days/iteration** (max capacity)
**Utilization:** Iteration 1 & 2 at 50d (83%), Iteration 3 at 47d (78%) — leaving buffer for testing, bug fixes, and integration.

---

## 2. Effort Breakdown by Iteration

### Iteration 1 — 36 functions, 50 person-days

**Focus:** Foundation — Authentication, Class CRUD, Content Basics, User Management

| Member | Tasks | Effort | Functions |
|--------|-------|--------|-----------|
| HuyMT | 6 | 10d | Create Class (2d), Update Class (2d), Delete Class (1d), Approve/Reject Student Requests (2d), View User List (2d), View Personal Schedule (Teacher) (1d) |
| Nghĩa | 6 | 10d | View Homepage (1d), Register Account (3d), Login (1d), Logout (1d), Forgot Password (2d), Change Password (2d) |
| AnhNHH | 8 | 10d | View Profile (1d), Update Profile (2d), View Notifications (1d), View Class Information (1d), View Student Information (1d), View Comment (1d), Upload Class Material (2d), View Class Material (1d) |
| ToanDV | 6 | 10d | Search Class (2d), Join Class (2d), Leave Class (1d), Remove Student (1d), Create Subscription (2d), Create Post (2d) |
| DuongNC | 10 | 10d | View Post (1d), Update Post (1d), Delete Post (1d), Create Comment (1d), Update Comment (1d), Delete Comment (1d), View Materials (1d), Download Materials (1d), Download Class Material (1d), Delete Class Material (1d) |

**Priority Distribution (Iteration 1):**

- Highest: 4 functions (7d)
- High: 9 functions (17d)
- Medium: 11 functions (14d)
- Low: 12 functions (12d)

### Iteration 2 — 24 functions, 50 person-days

**Focus:** Core Features — Scheduling, Attendance, Assignments, Grading, Resource Bank

| Member | Tasks | Effort | Functions |
|--------|-------|--------|-----------|
| HuyMT | 6 | 10d | View Class Schedule (Student) (2d), Update Class Schedule (2d), Delete Class Schedule (1d), View Personal Schedule (Student) (3d), Delete Assignment (1d), View Assignment (Teacher) (1d) |
| Nghĩa | 4 | 10d | Create Assignment Manual (3d), Create Assignment By Uploading Files (3d), Update Assignment (2d), Create Resource Bank (2d) |
| AnhNHH | 4 | 10d | Create Class Schedule (3d), View Class Schedule (Teacher) (2d), Take Attendance (3d), Edit Attendance (2d) |
| ToanDV | 5 | 10d | Submit Assignment (2d), View Grade Submissions (2d), Grade Manual Essay (2d), View Grades & Solutions (2d), View Student Dashboard (2d) |
| DuongNC | 5 | 10d | View Assignment (Student) (1d), Attempt Assignment (3d), Export Grades (2d), View Resource Bank (2d), Edit Resource Bank (2d) |

**Priority Distribution (Iteration 2):**

- Highest: 4 functions (11d)
- High: 9 functions (19d)
- Medium: 7 functions (14d)
- Low: 4 functions (6d)

### Iteration 3 — 21 functions, 47 person-days

**Focus:** Advanced Features — AI-powered tools, Analytics, Subscription, Virtual Meeting

| Member | Tasks | Effort | Functions |
|--------|-------|--------|-----------|
| HuyMT | 5 | 10d | Update User Status (2d), Reset User Password (2d), View System Dashboard (2d), View Revenue Dashboard (2d), View Transaction History (2d) |
| Nghĩa | 3 | 9d | Create Question With AI (4d), Grade Essay With AI Feedback (4d), Delete Question In Resource Bank (1d) |
| AnhNHH | 4 | 10d | Create Assignment With AI (3d), Create Question Manual (2d), Create Question By Importing Files (3d), Create Assignment By Importing From Resource Bank (2d) |
| ToanDV | 4 | 8d | Update Question In Resource Bank (2d), Download Resource Bank (2d), View Class Analytics (3d), Delete Resource Bank (1d) |
| DuongNC | 5 | 10d | Join Meeting (3d), Update Subscription (2d), Delete Subscription (1d), View Subscriptions (2d), Buy Subscription (2d) |

**Priority Distribution (Iteration 3):**

- Highest: 1 functions (3d)
- High: 7 functions (20d)
- Medium: 9 functions (19d)
- Low: 4 functions (5d)

---

## 3. Member Workload Analysis

### 3.1 Workload Per Iteration

| Member | Role | Iter 1 | Iter 2 | Iter 3 | Total |
|--------|------|--------|--------|--------|-------|
| HuyMT | PM/Scrum Master | 10d (6 tasks) | 10d (6 tasks) | 10d (5 tasks) | 30d |
| Nghĩa | Tech Lead/Dev | 10d (6 tasks) | 10d (4 tasks) | 9d (3 tasks) | 29d |
| AnhNHH | Developer | 10d (8 tasks) | 10d (4 tasks) | 10d (4 tasks) | 30d |
| ToanDV | Developer | 10d (6 tasks) | 10d (5 tasks) | 8d (4 tasks) | 28d |
| DuongNC | Developer | 10d (10 tasks) | 10d (5 tasks) | 10d (5 tasks) | 30d |

### 3.2 Workload Balance Justification

- **Iterations 1 & 2:** Every member is assigned exactly **10 person-days** — perfectly balanced.
- **Iteration 3:** Nghĩa has 9d and ToanDV has 8d. The **3-day buffer** (47d vs 50d capacity) is intentional:
  - Final iteration is reserved for integration testing, bug fixes, and documentation polish.
  - AI-related tasks (Nghĩa's 4d+4d) are high-risk and may need extra debugging time.
  - The buffer ensures the team is not overloaded during the critical final delivery phase.

### 3.3 Task Complexity Distribution Per Member

| Member | Simple | Medium | Complex | Avg Effort/Task |
|--------|--------|--------|---------|-----------------|
| HuyMT | 7 | 8 | 2 | 1.8d |
| Nghĩa | 4 | 7 | 2 | 2.2d |
| AnhNHH | 7 | 7 | 2 | 1.9d |
| ToanDV | 6 | 8 | 1 | 1.9d |
| DuongNC | 14 | 5 | 1 | 1.5d |

**Key Insight:** Complex tasks (AI features) are assigned to the **Tech Lead (Nghĩa)** and **experienced developers (AnhNHH)**, while simpler CRUD tasks go to other members — matching skill level to task complexity.

---

## 4. Complexity Level Classification

### 4.1 Simple (38 functions, 46d total, avg 1.2d)

**Description:** Standard CRUD operations, view-only screens, delete confirmations
**Effort Range:** 1-2 person-days
**Criteria:** Single API call, minimal UI logic, no complex validation

| Function | Est. Effort | Feature | Priority |
|----------|-------------|---------|----------|
| View Homepage | 1d | Authentication & User Profile | Highest |
| Login | 1d | Authentication & User Profile | Highest |
| Logout | 1d | Authentication & User Profile | Low |
| View Profile | 1d | Authentication & User Profile | High |
| View Notifications | 1d | Authentication & User Profile | Medium |
| Create Class | 2d | Class Management | Highest |
| Delete Class | 1d | Class Management | Low |
| View Personal Schedule (Teacher) | 1d | Authentication & User Profile | Medium |
| Search Class | 2d | Class Management | High |
| Leave Class | 1d | Class Management | Low |
| Remove Student | 1d | Administration & Subscription | Low |
| View Class Information | 1d | Class Management | Medium |
| View Student Information | 1d | Administration & Subscription | Medium |
| View Post | 1d | Course Content & Communication | Medium |
| Update Post | 1d | Course Content & Communication | Low |
| Delete Post | 1d | Course Content & Communication | Low |
| View Comment | 1d | Course Content & Communication | Low |
| Create Comment | 1d | Course Content & Communication | Medium |
| Update Comment | 1d | Course Content & Communication | Low |
| Delete Comment | 1d | Course Content & Communication | Low |
| View Class Material | 1d | Course Content & Communication | Medium |
| View Materials | 1d | Course Content & Communication | Medium |
| Download Materials | 1d | Course Content & Communication | Low |
| Download Class Material | 1d | Course Content & Communication | Low |
| Delete Class Material | 1d | Course Content & Communication | Low |
| Delete Class Schedule | 1d | Class Management | Low |
| Edit Attendance | 2d | Class Management | Medium |
| Delete Assignment | 1d | Assignments & Assessment | Low |
| View Assignment (Teacher) | 1d | Assignments & Assessment | Medium |
| View Assignment (Student) | 1d | Assignments & Assessment | High |
| View Grade Submissions | 2d | Assignments & Assessment | Medium |
| View Grades & Solutions | 2d | Assignments & Assessment | Medium |
| View Resource Bank | 2d | Resource Bank Management | High |
| Delete Question In Resource Bank | 1d | Resource Bank Management | Low |
| Delete Resource Bank | 1d | Resource Bank Management | Low |
| View Transaction History | 2d | Administration & Subscription | Low |
| Delete Subscription | 1d | Administration & Subscription | Low |
| View Subscriptions | 2d | Administration & Subscription | Medium |

### 4.2 Medium (35 functions, 77d total, avg 2.2d)

**Description:** Forms with validation, search/filter, file handling, scheduling
**Effort Range:** 2-3 person-days
**Criteria:** Multiple API calls, form validation, file upload/download, moderate UI complexity

| Function | Est. Effort | Feature | Priority |
|----------|-------------|---------|----------|
| Register Account | 3d | Authentication & User Profile | Highest |
| Forgot Password | 2d | Authentication & User Profile | High |
| Change Password | 2d | Authentication & User Profile | Medium |
| Update Profile | 2d | Authentication & User Profile | Medium |
| Update Class | 2d | Class Management | High |
| Approve/Reject Student Requests | 2d | Class Management | High |
| View User List | 2d | Administration & Subscription | High |
| Join Class | 2d | Class Management | High |
| Create Subscription | 2d | Administration & Subscription | High |
| Create Post | 2d | Course Content & Communication | Medium |
| Upload Class Material | 2d | Course Content & Communication | High |
| Create Class Schedule | 3d | Class Management | Highest |
| View Class Schedule (Teacher) | 2d | Class Management | High |
| View Class Schedule (Student) | 2d | Class Management | High |
| Update Class Schedule | 2d | Class Management | High |
| View Personal Schedule (Student) | 3d | Authentication & User Profile | Medium |
| Take Attendance | 3d | Class Management | High |
| Create Assignment Manual | 3d | Assignments & Assessment | Highest |
| Create Assignment By Uploading Files | 3d | Assignments & Assessment | Highest |
| Update Assignment | 2d | Assignments & Assessment | High |
| Attempt Assignment | 3d | Assignments & Assessment | High |
| Submit Assignment | 2d | Assignments & Assessment | High |
| Grade Manual Essay | 2d | Assignments & Assessment | Medium |
| View Student Dashboard | 2d | Assignments & Assessment | Low |
| Export Grades | 2d | Assignments & Assessment | Low |
| Create Resource Bank | 2d | Resource Bank Management | Highest |
| Edit Resource Bank | 2d | Resource Bank Management | Medium |
| Create Question Manual | 2d | Resource Bank Management | High |
| Update Question In Resource Bank | 2d | Resource Bank Management | Medium |
| Create Assignment By Importing From Resource Bank | 2d | Assignments & Assessment | High |
| Download Resource Bank | 2d | Resource Bank Management | Medium |
| Update User Status | 2d | Administration & Subscription | Medium |
| Reset User Password | 2d | Administration & Subscription | Medium |
| Update Subscription | 2d | Administration & Subscription | Medium |
| Buy Subscription | 2d | Administration & Subscription | High |

### 4.3 Complex (8 functions, 24d total, avg 3.0d)

**Description:** AI integration, analytics dashboards, real-time features, payment processing
**Effort Range:** 3-4 person-days
**Criteria:** External API integration (AI/payment), complex data aggregation, real-time communication

| Function | Est. Effort | Feature | Priority |
|----------|-------------|---------|----------|
| Create Question With AI | 4d | Resource Bank Management | High |
| Grade Essay With AI Feedback | 4d | Assignments & Assessment | High |
| Create Assignment With AI | 3d | Assignments & Assessment | Highest |
| Create Question By Importing Files | 3d | Resource Bank Management | High |
| View Class Analytics | 3d | Assignments & Assessment | Medium |
| Join Meeting | 3d | Course Content & Communication | High |
| View System Dashboard | 2d | Administration & Subscription | Medium |
| View Revenue Dashboard | 2d | Administration & Subscription | Medium |

---

## 5. Feature Area Analysis

| Feature | Functions | Effort | % of Total | Iterations |
|---------|----------|--------|------------|------------|
| Authentication & User Profile | 11 | 18d | 12% | Iter 1, Iter 2 |
| Class Management | 15 | 28d | 19% | Iter 1, Iter 2 |
| Course Content & Communication | 15 | 19d | 13% | Iter 1, Iter 3 |
| Assignments & Assessment | 17 | 38d | 26% | Iter 2, Iter 3 |
| Resource Bank Management | 10 | 21d | 14% | Iter 2, Iter 3 |
| Administration & Subscription | 13 | 23d | 16% | Iter 1, Iter 3 |

### 5.1 Sub-Feature Detail

#### Authentication & User Profile (11 functions, 18d)

**Sign Up & Sign In** (5 functions, 8d):
- View Homepage — Simple, 1d, Highest [Iter 1]
- Register Account — Medium, 3d, Highest [Iter 1]
- Login — Simple, 1d, Highest [Iter 1]
- Logout — Simple, 1d, Low [Iter 1]
- Forgot Password — Medium, 2d, High [Iter 1]
**Profile Management** (6 functions, 10d):
- Change Password — Medium, 2d, Medium [Iter 1]
- View Profile — Simple, 1d, High [Iter 1]
- Update Profile — Medium, 2d, Medium [Iter 1]
- View Notifications — Simple, 1d, Medium [Iter 1]
- View Personal Schedule (Teacher) — Simple, 1d, Medium [Iter 1]
- View Personal Schedule (Student) — Medium, 3d, Medium [Iter 2]

#### Class Management (15 functions, 28d)

**Class Administration** (3 functions, 5d):
- Create Class — Simple, 2d, Highest [Iter 1]
- Update Class — Medium, 2d, High [Iter 1]
- Delete Class — Simple, 1d, Low [Iter 1]
**Class Participation** (5 functions, 8d):
- Approve/Reject Student Requests — Medium, 2d, High [Iter 1]
- Search Class — Simple, 2d, High [Iter 1]
- Join Class — Medium, 2d, High [Iter 1]
- Leave Class — Simple, 1d, Low [Iter 1]
- View Class Information — Simple, 1d, Medium [Iter 1]
**Attendance & Scheduling** (7 functions, 15d):
- Create Class Schedule — Medium, 3d, Highest [Iter 2]
- View Class Schedule (Teacher) — Medium, 2d, High [Iter 2]
- View Class Schedule (Student) — Medium, 2d, High [Iter 2]
- Update Class Schedule — Medium, 2d, High [Iter 2]
- Delete Class Schedule — Simple, 1d, Low [Iter 2]
- Take Attendance — Medium, 3d, High [Iter 2]
- Edit Attendance — Simple, 2d, Medium [Iter 2]

#### Course Content & Communication (15 functions, 19d)

**Posts & Comments** (8 functions, 9d):
- Create Post — Medium, 2d, Medium [Iter 1]
- View Post — Simple, 1d, Medium [Iter 1]
- Update Post — Simple, 1d, Low [Iter 1]
- Delete Post — Simple, 1d, Low [Iter 1]
- View Comment — Simple, 1d, Low [Iter 1]
- Create Comment — Simple, 1d, Medium [Iter 1]
- Update Comment — Simple, 1d, Low [Iter 1]
- Delete Comment — Simple, 1d, Low [Iter 1]
**Learning Class Materials** (6 functions, 7d):
- Upload Class Material — Medium, 2d, High [Iter 1]
- View Class Material — Simple, 1d, Medium [Iter 1]
- View Materials — Simple, 1d, Medium [Iter 1]
- Download Materials — Simple, 1d, Low [Iter 1]
- Download Class Material — Simple, 1d, Low [Iter 1]
- Delete Class Material — Simple, 1d, Low [Iter 1]
**Virtual Meeting** (1 functions, 3d):
- Join Meeting — Complex, 3d, High [Iter 3]

#### Assignments & Assessment (17 functions, 38d)

**Assignment Management** (8 functions, 16d):
- Create Assignment Manual — Medium, 3d, Highest [Iter 2]
- Create Assignment By Uploading Files — Medium, 3d, Highest [Iter 2]
- Update Assignment — Medium, 2d, High [Iter 2]
- Delete Assignment — Simple, 1d, Low [Iter 2]
- View Assignment (Teacher) — Simple, 1d, Medium [Iter 2]
- View Assignment (Student) — Simple, 1d, High [Iter 2]
- Create Assignment With AI — Complex, 3d, Highest [Iter 3]
- Create Assignment By Importing From Resource Bank — Medium, 2d, High [Iter 3]
**Submission & Grading** (5 functions, 13d):
- Attempt Assignment — Medium, 3d, High [Iter 2]
- Submit Assignment — Medium, 2d, High [Iter 2]
- View Grade Submissions — Simple, 2d, Medium [Iter 2]
- Grade Manual Essay — Medium, 2d, Medium [Iter 2]
- Grade Essay With AI Feedback — Complex, 4d, High [Iter 3]
**Analytics & Results** (4 functions, 9d):
- View Grades & Solutions — Simple, 2d, Medium [Iter 2]
- View Student Dashboard — Medium, 2d, Low [Iter 2]
- Export Grades — Medium, 2d, Low [Iter 2]
- View Class Analytics — Complex, 3d, Medium [Iter 3]

#### Resource Bank Management (10 functions, 21d)

**Bank Operations** (5 functions, 9d):
- Create Resource Bank — Medium, 2d, Highest [Iter 2]
- View Resource Bank — Simple, 2d, High [Iter 2]
- Edit Resource Bank — Medium, 2d, Medium [Iter 2]
- Download Resource Bank — Medium, 2d, Medium [Iter 3]
- Delete Resource Bank — Simple, 1d, Low [Iter 3]
**Question Management** (5 functions, 12d):
- Create Question With AI — Complex, 4d, High [Iter 3]
- Create Question Manual — Medium, 2d, High [Iter 3]
- Create Question By Importing Files — Complex, 3d, High [Iter 3]
- Update Question In Resource Bank — Medium, 2d, Medium [Iter 3]
- Delete Question In Resource Bank — Simple, 1d, Low [Iter 3]

#### Administration & Subscription (13 functions, 23d)

**User & System Management** (6 functions, 10d):
- View User List — Medium, 2d, High [Iter 1]
- Remove Student — Simple, 1d, Low [Iter 1]
- View Student Information — Simple, 1d, Medium [Iter 1]
- Update User Status — Medium, 2d, Medium [Iter 3]
- Reset User Password — Medium, 2d, Medium [Iter 3]
- View System Dashboard — Complex, 2d, Medium [Iter 3]
**Subscription Management** (7 functions, 13d):
- Create Subscription — Medium, 2d, High [Iter 1]
- View Revenue Dashboard — Complex, 2d, Medium [Iter 3]
- View Transaction History — Simple, 2d, Low [Iter 3]
- Update Subscription — Medium, 2d, Medium [Iter 3]
- Delete Subscription — Simple, 1d, Low [Iter 3]
- View Subscriptions — Simple, 2d, Medium [Iter 3]
- Buy Subscription — Medium, 2d, High [Iter 3]

---

## 6. Priority Analysis

Priority assignment follows a dependency-driven approach:

| Priority | Meaning | Functions | Effort | Strategy |
|----------|---------|----------|--------|----------|
| Highest | Must-have foundation, blocks other features | 9 | 21d | Must-have foundation, blocks other features |
| High | Core functionality, depends on Highest items | 25 | 56d | Core functionality, depends on Highest items |
| Medium | Important but not blocking other features | 27 | 47d | Important but not blocking other features |
| Low | Nice-to-have, can be deferred if needed | 20 | 23d | Nice-to-have, can be deferred if needed |

### 6.1 Priority Distribution by Iteration

| Iteration | Highest | High | Medium | Low |
|-----------|---------|------|--------|-----|
| Iteration 1 | 4 (7d) | 9 (17d) | 11 (14d) | 12 (12d) |
| Iteration 2 | 4 (11d) | 9 (19d) | 7 (14d) | 4 (6d) |
| Iteration 3 | 1 (3d) | 7 (20d) | 9 (19d) | 4 (5d) |

**Validation:** Highest-priority items are concentrated in Iterations 1 & 2 (foundation first), while Iteration 3 focuses on advanced features (AI, analytics) which depend on the base platform.

---

## 7. Iteration Dependency Chain

The iteration ordering follows a strict dependency chain to avoid blocking:

### Iteration 1 → Iteration 2 Dependencies

| Iter 1 (Prerequisite) | Iter 2 (Depends On) | Reason |
|----------------------|---------------------|--------|
| Create Class | Create Class Schedule | Schedule belongs to a class |
| Create Class | Take Attendance | Attendance is per class session |
| Register Account / Login | Create Assignment Manual | Teacher must be authenticated |
| Create Class | Submit Assignment | Students submit within a class |
| Create Class | Upload Class Material | Materials belong to a class |
| Join Class | View Class Schedule (Student) | Student must be enrolled |
| Join Class | View Personal Schedule (Student) | Aggregates from enrolled classes |

### Iteration 2 → Iteration 3 Dependencies

| Iter 2 (Prerequisite) | Iter 3 (Depends On) | Reason |
|----------------------|---------------------|--------|
| Create Resource Bank | Create Question With AI | Questions go into resource bank |
| Create Resource Bank | Create Question Manual | Questions go into resource bank |
| Create Assignment Manual | Grade Essay With AI Feedback | Must have assignments to grade |
| Submit Assignment | View Class Analytics | Analytics aggregate submission data |
| Create Resource Bank | Create Assignment By Importing From Resource Bank | Needs existing bank |
| Create Subscription (Iter 1) | Buy Subscription | Plans must exist before purchase |

---

## 8. Effort Estimation Methodology

### 8.1 Estimation Criteria

Each function's effort was estimated based on:

| Factor | Simple (1d) | Medium (2-3d) | Complex (3-4d) |
|--------|-------------|---------------|----------------|
| **UI Components** | 1-2 basic elements | 3-5 elements with validation | 5+ elements, dynamic/interactive |
| **API Calls** | 1 simple GET/POST | 2-3 calls with logic | Multiple calls + external services |
| **Data Handling** | Read-only display | CRUD with validation | Aggregation, transformation, AI |
| **Testing** | Basic happy path | Edge cases + validation | Integration + error handling |
| **Examples** | View Profile, Logout | Create Class, Join Class | AI Question Generator, Analytics |

### 8.2 Consistency Cross-Check

Similar functions were compared to ensure consistent estimation:

| Pattern | Functions | Effort | Rationale |
|---------|----------|--------|-----------|
| **View-only screens** | View Profile, View Post, View Comment, View Materials | 1d each | Single API call, read-only display |
| **Delete operations** | Delete Class, Delete Post, Delete Comment, Delete Assignment | 1d each | Confirmation dialog + single API call |
| **Search/Filter lists** | Search Class, View User List | 2d each | Search bar + filters + paginated results |
| **Create with form** | Create Class, Create Post, Create Comment | 1-2d | Form validation + single API call |
| **Create with upload** | Upload Class Material, Create Assignment By Uploading Files | 2-3d | File handling + validation + storage |
| **Schedule management** | Create/Update/View Class Schedule | 2-3d | Calendar UI + time validation + recurring logic |
| **AI-powered features** | Create Question With AI, Grade Essay With AI, Create Assignment With AI | 3-4d | External AI API + prompt engineering + result parsing |
| **Dashboard/Analytics** | View System Dashboard, View Revenue Dashboard, View Class Analytics | 2-3d | Data aggregation + chart rendering |

---

## 9. Risk & Buffer Analysis

| Metric | Value |
|--------|-------|
| Total Capacity (3 iterations × 60d) | 180 person-days |
| Total Estimated Effort | 147 person-days |
| **Buffer** | **33 person-days (18%)** |

### Buffer Usage Plan

| Buffer Allocation | Days | Purpose |
|-------------------|------|---------|
| Integration Testing | 10d | End-to-end testing across all features |
| Bug Fixes | 10d | Fixing issues found during testing |
| Code Review & Refactoring | 6d | Quality assurance and tech debt |
| Documentation | 4d | API docs, user guides, deployment notes |
| Contingency | 3d | Unexpected issues or scope changes |
| **Total Buffer** | **33d** | |

### Risk Factors

| Risk | Impact | Mitigation |
|------|--------|------------|
| AI API integration delays | High | 3d buffer in Iter 3 + fallback to manual features |
| Payment gateway complexity | Medium | Buy Subscription uses standard payment SDK |
| Real-time meeting integration | Medium | Join Meeting uses external meeting link (no custom WebRTC) |
| Team member unavailability | Low | Balanced workload allows task reassignment |

---

## 10. Complete Function List

| # | Function/Screen | Level | Effort | Iteration | Incharge | Priority | Feature |
|---|----------------|-------|--------|-----------|----------|----------|---------|
| 1 | View Homepage | Simple | 1d | Iter 1 | Nghĩa | Highest | Authentication & User Profile |
| 2 | Register Account | Medium | 3d | Iter 1 | Nghĩa | Highest | Authentication & User Profile |
| 3 | Login | Simple | 1d | Iter 1 | Nghĩa | Highest | Authentication & User Profile |
| 4 | Logout | Simple | 1d | Iter 1 | Nghĩa | Low | Authentication & User Profile |
| 5 | Forgot Password | Medium | 2d | Iter 1 | Nghĩa | High | Authentication & User Profile |
| 6 | Change Password | Medium | 2d | Iter 1 | Nghĩa | Medium | Authentication & User Profile |
| 7 | View Profile | Simple | 1d | Iter 1 | AnhNHH | High | Authentication & User Profile |
| 8 | Update Profile | Medium | 2d | Iter 1 | AnhNHH | Medium | Authentication & User Profile |
| 9 | View Notifications | Simple | 1d | Iter 1 | AnhNHH | Medium | Authentication & User Profile |
| 10 | Create Class | Simple | 2d | Iter 1 | HuyMT | Highest | Class Management |
| 11 | Update Class | Medium | 2d | Iter 1 | HuyMT | High | Class Management |
| 12 | Delete Class | Simple | 1d | Iter 1 | HuyMT | Low | Class Management |
| 13 | Approve/Reject Student Requests | Medium | 2d | Iter 1 | HuyMT | High | Class Management |
| 14 | View User List | Medium | 2d | Iter 1 | HuyMT | High | Administration & Subscription |
| 15 | View Personal Schedule (Teacher) | Simple | 1d | Iter 1 | HuyMT | Medium | Authentication & User Profile |
| 16 | Search Class | Simple | 2d | Iter 1 | ToanDV | High | Class Management |
| 17 | Join Class | Medium | 2d | Iter 1 | ToanDV | High | Class Management |
| 18 | Leave Class | Simple | 1d | Iter 1 | ToanDV | Low | Class Management |
| 19 | Remove Student | Simple | 1d | Iter 1 | ToanDV | Low | Administration & Subscription |
| 20 | Create Subscription | Medium | 2d | Iter 1 | ToanDV | High | Administration & Subscription |
| 21 | View Class Information | Simple | 1d | Iter 1 | AnhNHH | Medium | Class Management |
| 22 | View Student Information | Simple | 1d | Iter 1 | AnhNHH | Medium | Administration & Subscription |
| 23 | Create Post | Medium | 2d | Iter 1 | ToanDV | Medium | Course Content & Communication |
| 24 | View Post | Simple | 1d | Iter 1 | DuongNC | Medium | Course Content & Communication |
| 25 | Update Post | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 26 | Delete Post | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 27 | View Comment | Simple | 1d | Iter 1 | AnhNHH | Low | Course Content & Communication |
| 28 | Create Comment | Simple | 1d | Iter 1 | DuongNC | Medium | Course Content & Communication |
| 29 | Update Comment | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 30 | Delete Comment | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 31 | Upload Class Material | Medium | 2d | Iter 1 | AnhNHH | High | Course Content & Communication |
| 32 | View Class Material | Simple | 1d | Iter 1 | AnhNHH | Medium | Course Content & Communication |
| 33 | View Materials | Simple | 1d | Iter 1 | DuongNC | Medium | Course Content & Communication |
| 34 | Download Materials | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 35 | Download Class Material | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 36 | Delete Class Material | Simple | 1d | Iter 1 | DuongNC | Low | Course Content & Communication |
| 37 | Create Class Schedule | Medium | 3d | Iter 2 | AnhNHH | Highest | Class Management |
| 38 | View Class Schedule (Teacher) | Medium | 2d | Iter 2 | AnhNHH | High | Class Management |
| 39 | View Class Schedule (Student) | Medium | 2d | Iter 2 | HuyMT | High | Class Management |
| 40 | Update Class Schedule | Medium | 2d | Iter 2 | HuyMT | High | Class Management |
| 41 | Delete Class Schedule | Simple | 1d | Iter 2 | HuyMT | Low | Class Management |
| 42 | View Personal Schedule (Student) | Medium | 3d | Iter 2 | HuyMT | Medium | Authentication & User Profile |
| 43 | Take Attendance | Medium | 3d | Iter 2 | AnhNHH | High | Class Management |
| 44 | Edit Attendance | Simple | 2d | Iter 2 | AnhNHH | Medium | Class Management |
| 45 | Create Assignment Manual | Medium | 3d | Iter 2 | Nghĩa | Highest | Assignments & Assessment |
| 46 | Create Assignment By Uploading Files | Medium | 3d | Iter 2 | Nghĩa | Highest | Assignments & Assessment |
| 47 | Update Assignment | Medium | 2d | Iter 2 | Nghĩa | High | Assignments & Assessment |
| 48 | Delete Assignment | Simple | 1d | Iter 2 | HuyMT | Low | Assignments & Assessment |
| 49 | View Assignment (Teacher) | Simple | 1d | Iter 2 | HuyMT | Medium | Assignments & Assessment |
| 50 | View Assignment (Student) | Simple | 1d | Iter 2 | DuongNC | High | Assignments & Assessment |
| 51 | Attempt Assignment | Medium | 3d | Iter 2 | DuongNC | High | Assignments & Assessment |
| 52 | Submit Assignment | Medium | 2d | Iter 2 | ToanDV | High | Assignments & Assessment |
| 53 | View Grade Submissions | Simple | 2d | Iter 2 | ToanDV | Medium | Assignments & Assessment |
| 54 | Grade Manual Essay | Medium | 2d | Iter 2 | ToanDV | Medium | Assignments & Assessment |
| 55 | View Grades & Solutions | Simple | 2d | Iter 2 | ToanDV | Medium | Assignments & Assessment |
| 56 | View Student Dashboard | Medium | 2d | Iter 2 | ToanDV | Low | Assignments & Assessment |
| 57 | Export Grades | Medium | 2d | Iter 2 | DuongNC | Low | Assignments & Assessment |
| 58 | Create Resource Bank | Medium | 2d | Iter 2 | Nghĩa | Highest | Resource Bank Management |
| 59 | View Resource Bank | Simple | 2d | Iter 2 | DuongNC | High | Resource Bank Management |
| 60 | Edit Resource Bank | Medium | 2d | Iter 2 | DuongNC | Medium | Resource Bank Management |
| 61 | Create Question With AI | Complex | 4d | Iter 3 | Nghĩa | High | Resource Bank Management |
| 62 | Grade Essay With AI Feedback | Complex | 4d | Iter 3 | Nghĩa | High | Assignments & Assessment |
| 63 | Create Assignment With AI | Complex | 3d | Iter 3 | AnhNHH | Highest | Assignments & Assessment |
| 64 | Create Question Manual | Medium | 2d | Iter 3 | AnhNHH | High | Resource Bank Management |
| 65 | Create Question By Importing Files | Complex | 3d | Iter 3 | AnhNHH | High | Resource Bank Management |
| 66 | Update Question In Resource Bank | Medium | 2d | Iter 3 | ToanDV | Medium | Resource Bank Management |
| 67 | Delete Question In Resource Bank | Simple | 1d | Iter 3 | Nghĩa | Low | Resource Bank Management |
| 68 | Create Assignment By Importing From Resource Bank | Medium | 2d | Iter 3 | AnhNHH | High | Assignments & Assessment |
| 69 | Download Resource Bank | Medium | 2d | Iter 3 | ToanDV | Medium | Resource Bank Management |
| 70 | View Class Analytics | Complex | 3d | Iter 3 | ToanDV | Medium | Assignments & Assessment |
| 71 | Delete Resource Bank | Simple | 1d | Iter 3 | ToanDV | Low | Resource Bank Management |
| 72 | Join Meeting | Complex | 3d | Iter 3 | DuongNC | High | Course Content & Communication |
| 73 | Update User Status | Medium | 2d | Iter 3 | HuyMT | Medium | Administration & Subscription |
| 74 | Reset User Password | Medium | 2d | Iter 3 | HuyMT | Medium | Administration & Subscription |
| 75 | View System Dashboard | Complex | 2d | Iter 3 | HuyMT | Medium | Administration & Subscription |
| 76 | View Revenue Dashboard | Complex | 2d | Iter 3 | HuyMT | Medium | Administration & Subscription |
| 77 | View Transaction History | Simple | 2d | Iter 3 | HuyMT | Low | Administration & Subscription |
| 78 | Update Subscription | Medium | 2d | Iter 3 | DuongNC | Medium | Administration & Subscription |
| 79 | Delete Subscription | Simple | 1d | Iter 3 | DuongNC | Low | Administration & Subscription |
| 80 | View Subscriptions | Simple | 2d | Iter 3 | DuongNC | Medium | Administration & Subscription |
| 81 | Buy Subscription | Medium | 2d | Iter 3 | DuongNC | High | Administration & Subscription |

---

*Report generated from WSB.csv — Learnify Project, February 2026*