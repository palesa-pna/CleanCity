from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/nompu/OneDrive/Desktop/Assignments/CleanCity/index.html")

wait = WebDriverWait(driver, 10)

# Navigate to login page explicitly
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='login']")))
login_link.click()


# --- Login ---
email_input = wait.until(EC.element_to_be_clickable((By.ID, "login-email")))
email_input.send_keys("user@cleancity.com")

password_input = driver.find_element(By.ID, "login-password")
password_input.send_keys("password123")

login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

# Wait for dashboard link to appear and click it
dashboard_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='dashboard']")))
dashboard_link.click()

# Wait for dashboard page content to load (table)
wait.until(EC.visibility_of_element_located((By.ID, "requests-table")))

# Interact with status filter
status_filter = Select(driver.find_element(By.ID, "statusFilter"))
location_filter = Select(driver.find_element(By.ID, "locationFilter"))

# Define filter values to test
status_options = [opt.get_attribute("value") for opt in status_filter.options]
location_options = [opt.get_attribute("value") for opt in location_filter.options]

print("Applying filters and checking results...")

for status in status_options:
    status_filter.select_by_value(status)
    time.sleep(1)  # wait for filtering effect (adjust as needed)

    for location in location_options:
        location_filter.select_by_value(location)
        time.sleep(1)

        # Count visible rows in table body
        rows = driver.find_elements(By.CSS_SELECTOR, "#requests-tbody tr")
        visible_rows = [row for row in rows if row.is_displayed()]

        print(f"Filter Status='{status}', Location='{location}': {len(visible_rows)} visible rows")

        # (Optional) Interact with first row if exists
        if visible_rows:
            first_row = visible_rows[0]
            first_row.click()
            time.sleep(0.5)

# Close browser after test
driver.quit()
