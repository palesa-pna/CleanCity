from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time, os

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Load local CleanCity
driver.get("file:///C:/Users/nompu/OneDrive/Desktop/Assignments/CleanCity/index.html")

# ---- STEP 1: Login first ----
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='login']")))
login_link.click()

wait.until(EC.presence_of_element_located((By.ID, "login-form")))
driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
driver.find_element(By.ID, "login-password").send_keys("password123")
driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()

# Wait for dashboard link to confirm login
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-page='dashboard']")))
print("✅ Logged in successfully.")

# ---- STEP 2: Navigate to Feedback page ----
feedback_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='feedback']")))
feedback_link.click()

# Wait until feedback form is visible
wait.until(EC.visibility_of_element_located((By.ID, "feedback-form")))
print("✅ Feedback page loaded.")

# ---- STEP 3: Fill and submit feedback form ----
driver.find_element(By.ID, "requestId").send_keys("REQ001")
driver.find_element(By.ID, "reason").send_keys("Missed Pickup")
driver.find_element(By.ID, "comments").send_keys("Truck never arrived at scheduled time.")

driver.find_element(By.CSS_SELECTOR, "#feedback-form button[type='submit']").click()

# ---- STEP 4: Wait for success message ----
success_message = wait.until(EC.visibility_of_element_located((By.ID, "feedback-success")))
print("✅ Feedback submitted! Message:", success_message.text)

# Optionally take screenshot
os.makedirs("screenshots", exist_ok=True)
screenshot_path = os.path.join("screenshots", f"feedback_success_{int(time.time())}.png")
driver.save_screenshot(screenshot_path)
print(f"📸 Screenshot saved: {screenshot_path}")

time.sleep(3)
driver.quit()
