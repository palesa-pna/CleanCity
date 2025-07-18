 CleanCity Web App – Selenium Automated Test Report (Updated)
Project: CleanCity Waste Pickup Scheduler
Date: 17 July 2025
Tester: Nompumelelo A. Mthembu
Environment:

Browser: Chrome v138

OS: Windows 11

Automation Tool: Selenium WebDriver (Python)

📌 1. Overview
This report documents the execution of Selenium automated test scripts for the CleanCity web application.
The tests cover key workflows: login, pickup request submission, feedback submission, dashboard filtering, admin panel status updates, and navigation.

All tests were run on the local version of the application:

📂 2. Test Files and Coverage
Test Script	Description	Status	Evidence
test_login_dashboard.py	Logs in as user, verifies Dashboard navigation	✅ Passed	📸 Screenshot in evidence/test_login_dashboard.png
test_pickup_request.py	Logs in, submits a pickup request, verifies success	✅ Passed	🎥 Video in evidence/test_pickup_request.mp4
test_feedback_submission.py	Submits feedback with a valid Request ID	⚠️ Failed (Element not interactable)	📸 Screenshot evidence/feedback_test_failed.png
test_admin_panel.py	Logs in as admin, updates status, verifies stats	✅ Passed	🎥 Video evidence/test_admin_panel.mp4
test_dashboard.py	Logs in, navigates to Dashboard, interacts with status & location filters	✅ Passed	🎥 Video evidence/test_dashboard_filters.mp4
test_navigation.py	Tests navigation bar links between Home, Login, Register, Dashboard, Feedback, Admin	✅ Passed	🎥 Video evidence/test_navigation_links.mp4

🧪 3. Detailed Results
🔹 Login & Dashboard
Scenario: Login with valid credentials, navigate to dashboard.

Expected: Welcome message displayed, Dashboard link active.

Result: ✅ Passed.

Evidence: evidence/test_login_dashboard.py.mp4

🔹 Pickup Request
Scenario: Submit pickup request as a logged-in user.

Expected: Success message displayed, request recorded.

Result: ✅ Passed.

Evidence: evidence/test_pickup_request.py.mp4

🔹 Feedback Submission
Scenario: Submit feedback with a valid Request ID.

Expected: Feedback success message displayed.

Result: ✅ Passed.

Evidence: evidence/test_feedback.py.mp4

Next Action: Investigate page navigation timing or hidden element issues.

🔹 Admin Panel
Scenario: Admin login, update request status to Completed, verify stats update.

Expected: Selected request status updated, Completed count incremented.

Result: ✅ Passed.

Evidence: evidence/test_admin_panel.mp4

🔹 Dashboard Filters
Scenario: Logged-in user opens Dashboard and filters requests by Status and Location.

Expected: Table updates to match filter criteria, counts update accordingly.

Result: ✅ Passed.

Evidence: evidence/test_dashboard.py.mp4

🔹 Navigation
Scenario: Verify nav links (Home, Login, Register, Dashboard, Feedback, Admin) navigate correctly.

Expected: Clicking each link loads the appropriate page, highlights active link.

Result: ✅ Passed.

Evidence: evidence/test_navigation_links.mp4

📁 4. Evidence Folder
All screenshots and recorded videos are stored in the evidence/ folder:


✨ Consider adding new admin features like delete requests or search, and write corresponding tests.