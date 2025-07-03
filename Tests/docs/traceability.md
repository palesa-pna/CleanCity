# 🔗 Requirements Traceability Matrix (RTM)

**Project:** Clean City  
**Last Updated:** 2025-07-03  
**Purpose:** This document maps user stories and requirements to their corresponding test cases to ensure complete test coverage.

---

## 📄 Key

- **Story ID**: Reference from Jira or GitHub Projects  
- **Requirement Description**: Functional or non-functional requirement  
- **Test Case ID**: Reference to a specific test in your `/tests/` directory or manual test case list  
- **Status**: `✅ Covered`, `⚠️ Partial`, or `❌ Missing`  
- **Test Type**: `Unit`, `E2E`, `Manual`, `Accessibility`, etc.  

---

## 📊 Traceability Table

| Story ID | Requirement Description                    | Test Case ID(s)            | Status   | Test Type     |
|----------|---------------------------------------------|----------------------------|----------|---------------|
| US-001   | Users can register with email & password    | TC-AUTH-01, TC-AUTH-02     | ✅ Covered | E2E, Unit     |
| US-002   | Admin can manage user roles                 | TC-ADMIN-05                | ✅ Covered | E2E           |
| US-003   | Users can schedule waste pickup             | TC-WASTE-03, TC-WASTE-04   | ✅ Covered | Manual, E2E   |
| US-004   | App supports keyboard-only navigation       | TC-A11Y-01, TC-A11Y-04     | ⚠️ Partial | Accessibility |
| US-005   | Users can comment on blog posts             | TC-BLOG-02, TC-BLOG-03     | ✅ Covered | E2E, Manual   |
| US-006   | Dashboard shows real-time stats             | TC-DASH-01                 | ❌ Missing | TBD           |
| NFR-001  | Load time under 2s for 95% of users         | TC-LOAD-01                 | ✅ Covered | Performance   |
| NFR-002  | Passwords are encrypted                     | TC-SEC-01                  | ✅ Covered | Unit, Manual  |
| A11Y-001 | Screen reader support for all buttons       | TC-A11Y-02                 | ✅ Covered | Accessibility |

---

## 📝 Notes

- TC-DASH-01 test case is pending due to backend mock limitations.  
- All accessibility issues will be verified via NVDA and `axe-core` scans.  
- Stories marked ⚠️ will be revisited in Sprint 2.

---

