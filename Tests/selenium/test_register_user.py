from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver, capture_screenshot
import time

APP_URL = "https://cleancityqa.netlify.app/"

driver = get_driver()
try:
    driver.get(APP_URL)
    # Navigate to Register page
    driver.find_element(By.CSS_SELECTOR, "a[data-page='register']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "register-form"))
    )
    capture_screenshot(driver, "register_page_loaded")

    # Fill in fields
    driver.find_element(By.ID, "register-name").send_keys("Test User")
    driver.find_element(By.ID, "register-email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "register-password").send_keys("pass123")
    driver.find_element(By.ID, "register-confirm-password").send_keys("differentpass")
    capture_screenshot(driver, "register_form_filled")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "#register-form button[type='submit']").click()
    time.sleep(4)
    capture_screenshot(driver, "register_after_submit")

    # Check for error alert
    error_div = driver.find_element(By.ID, "register-error")
    assert error_div.is_displayed(), "Expected register error message not shown"
    print("[PASS] Register invalid scenario shows error message.")
except Exception as e:
    capture_screenshot(driver, "register_test_failed")
    print("[FAIL] Register test:", e)
finally:
    driver.quit()
