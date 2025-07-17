from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver, capture_screenshot
import time

APP_URL = "https://cleancityqa.netlify.app/"

driver = get_driver()
try:
    driver.get(APP_URL)
    # Navigate to Feedback page
    driver.find_element(By.CSS_SELECTOR, "a[data-page='feedback']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "feedback-form"))
    )
    capture_screenshot(driver, "feedback_page_loaded")

    # Fill in fields
    driver.find_element(By.ID, "requestId").send_keys("REQ001")
    driver.find_element(By.ID, "reason").send_keys("Missed Pickup")
    driver.find_element(By.ID, "comments").send_keys("Truck never came.")
    capture_screenshot(driver, "feedback_form_filled")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "#feedback-form button[type='submit']").click()
    time.sleep(10)
    capture_screenshot(driver, "feedback_after_submit")

    # Check for success alert
    success_div = driver.find_element(By.ID, "feedback-success")
    assert success_div.is_displayed(), "Expected feedback success message not shown"
    print("[PASS] Feedback form submitted successfully.")
except Exception as e:
    capture_screenshot(driver, "feedback_test_failed")
    print("[FAIL] Feedback test:", e)
finally:
    driver.quit()
