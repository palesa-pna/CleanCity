from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# --- Setup ---
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///C:/Users/nompu/OneDrive/Desktop/Assignments/CleanCity/index.html")
wait = WebDriverWait(driver, 10)

# --- Login as admin ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='login']"))).click()
wait.until(EC.presence_of_element_located((By.ID, "login-email"))).send_keys("admin@cleancity.com")
driver.find_element(By.ID, "login-password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()

# --- Wait for dashboard link to appear ---
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='admin']"))).click()

# --- Test updating a request status (assumes at least one request exists) ---
try:
    # Wait for select options to populate
    request_select = wait.until(EC.presence_of_element_located((By.ID, "requestSelect")))
    options_list = request_select.find_elements(By.TAG_NAME, "option")
    if len(options_list) > 1:
        # Choose the first valid request
        options_list[1].click()
        # Set status
        driver.find_element(By.ID, "statusSelect").click()
        driver.find_element(By.CSS_SELECTOR, "#statusSelect option[value='Scheduled']").click()
        update_btn = driver.find_element(By.ID, "updateStatusBtn")
        update_btn.click()
        print("[PASS] Updated request status successfully.")
    else:
        print("[INFO] No requests found to update.")
except Exception as e:
    print("[FAIL] Admin status update test failed:", e)

time.sleep(3)
driver.quit()
