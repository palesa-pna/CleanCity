Cypress Test Report – E2E Auth → Dashboard
CleanCity – Waste Pickup Scheduler
Test Scenario: End‑to‑End Authentication flow (Login → Dashboard)

Tools Used
Tool	Purpose
Cypress 14.5.1	End‑to‑end testing framework
Node.js v22.14.0	Runtime environment
npm	Dependency management
Electron 130 (Headless)	Browser used by Cypress in headless mode
CleanCity Web App	Hosted at https://cleancityqa.netlify.app/


Test Environment
Component	Version / Info
OS	Windows 11 x64
Node.js	v22.14.0
npm	10.x
Cypress	14.5.1
Browser	Electron (Headless)
Directory	C:\CleanCity
Test Spec	cypress/e2e/auth_dashboard.cy.js

E2E Test Case
Test Name: should log in and navigate to dashboard successfully

Steps
1. Visit Login Page
2. Navigate to https://cleancityqa.netlify.app/
3. Enter valid credentials
4. Email: user@cleancity.com
5. Password: password123
6. Submit login form, assert dashboard is displayed
  Check that dashboard elements (#dashboard-page) are visible.

Expected Result
User is successfully redirected to Dashboard.

Dashboard content is visible (e.g., Pickup Requests table).

**Test Results**
|Status 	| Duration	| Screenshot    |
|---------|-----------|---------------|
|Passed   |	8.5s	    |See below      |

Run Command:

npx cypress run --e2e --spec "cypress/e2e/auth_dashboard.cy.js"

Screenshots
By default, Cypress saves screenshots in:
C:\CleanCity\cypress\screenshots\


How to Enable Screenshots
Open cypress.config.js (or cypress.config.mjs):

js

module.exports = {
  e2e: {
    screenshotOnRunFailure: true,
    screenshotsFolder: "cypress/screenshots",
    video: false,
  },
};
Run test in headless mode:



npx cypress run
📷 Sample Screenshot Locations
(Below are examples assuming screenshots were captured)

Test Step	Screenshot Path
Before Login Submit	cypress/screenshots/before-login.png
After Login Submit	cypress/screenshots/after-login.png
Dashboard Loaded	cypress/screenshots/dashboard-loaded.png



🛠 Environment Setup Instructions
 1. Install Node.js

Verify:

node -v
npm -v

2. Install Cypress

cd C:\CleanCity
npm init -y
npm install cypress --save-dev

3. Run Cypress

npx cypress open
Headless mode (CI):


npx cypress run --e2e --spec "cypress/e2e/auth_dashboard.cy.js"

4. View Screenshots
After running tests:

makefile
C:\CleanCity\cypress\screenshots\
