from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_driver, capture_screenshot
import time

APP_URL = "https://cleancityqa.netlify.app/"

driver = get_driver()
try:
    driver.get(APP_URL)
    # Navigate to Home page (pickup form)
    driver.find_element(By.CSS_SELECTOR, "a[data-page='home']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pickup-form"))
    )
    capture_screenshot(driver, "pickup_page_loaded")

    # Leave required fields blank and submit
    driver.find_element(By.CSS_SELECTOR, "#pickup-form button[type='submit']").click()
    time.sleep(3)
    capture_screenshot(driver, "pickup_submit_with_empty_fields")


    assert driver.find_element(By.ID, "pickup-form").is_displayed()
    print("[PASS] Pickup form validation prevents empty submission.")
except Exception as e:
    capture_screenshot(driver, "pickup_form_failed")
    print("[FAIL] Pickup form test:", e)
finally:
    driver.quit()
