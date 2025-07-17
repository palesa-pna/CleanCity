
## CleanCity Test Schedule

| **Phase**               | **Description**                                                                                  | **Tools/Approach**                           | **Deadline**  |
|------------------------ |----------------------------------------------------------------------------------------------- |----------------------------------------------|--------------|
| **Unit Testing**        | Test core logic for correctness and reliability.                                                | Jest (JavaScript), pytest (Python)           | 2025-07-06   |
| **API & E2E Testing**   | Simulate API interactions (using localStorage mocks); test complete user flows end-to-end.      | Cypress, Jest, mocked APIs/localStorage      | 2025-07-10   |
| **Accessibility Review**| Ensure compliance with WCAG 2.1 AA; test with automated tools and screen readers.               | axe-core, NVDA, VoiceOver                    | 2025-07-14   |
| **Load Testing**        | Assess performance under simulated load (10,000 concurrent users).                              | k6                                           | 2025-07-15   |
| **Closure & Reporting** | Analyze test results, document bugs, finalize reports, and deliver a summary to stakeholders.   | Jira/GitHub Projects, documentation tools     | 2025-07-16   |

---

### Test Coverage Includes
- **Authentication:** Registration, login, password/session handling, user roles
- **Waste Pickup Features:** Scheduling, management, validation, data persistence
- **Dashboard & Analytics:** Data visualization, gamification, real-time updates
- **Content System:** Blogs, comments, quizzes, moderation workflows
- **User Management:** Profiles, admin panel, notifications
- **Accessibility:** Cross-browser and cross-device compatibility, WCAG 2.1 compliance
- **Performance:** Load, stress, and scalability

### Testing Management & Execution
- **Management:** Jira or GitHub Projects for tracking.
- **Automation:** Jest, Cypress, k6 for automated testing.
- **Manual Testing:** Exploratory, accessibility, and real-device testing.
- **CI/CD Integration:** All tests run automatically via GitHub Actions workflows.



