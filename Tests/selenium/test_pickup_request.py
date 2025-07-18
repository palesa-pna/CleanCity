from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

# 🔧 Chrome options (ignore cert errors if needed)
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

# 🚀 Start browser
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 📂 Load your local CleanCity HTML
driver.get("file:///C:/Users/nompu/OneDrive/Desktop/Assignments/CleanCity/index.html")

# Explicit wait
wait = WebDriverWait(driver, 10)

# ✨ STEP 1: Go to Login Page
login_link = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='login']"))
)
login_link.click()

# ✨ STEP 2: Fill Login Form
wait.until(EC.presence_of_element_located((By.ID, "login-form")))
driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
driver.find_element(By.ID, "login-password").send_keys("password123")
driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()

# ✅ Wait until dashboard link appears (indicating login success)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-page='dashboard']")))
print("✅ Login successful!")

# ✨ STEP 3: Navigate to Home page (pickup form)
home_link = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-page='home']"))
)
home_link.click()

# ✨ STEP 4: Wait for pickup form to appear
wait.until(EC.presence_of_element_located((By.ID, "pickup-form")))

# ✨ STEP 5: Fill Pickup Form
driver.find_element(By.ID, "fullName").send_keys("John Doe")
Select(driver.find_element(By.ID, "location")).select_by_visible_text("Nairobi")
driver.find_element(By.CSS_SELECTOR, "input[name='wasteType'][value='General']").click()
driver.find_element(By.ID, "preferredDate").send_keys("2025-07-20")

# ✨ STEP 6: Submit Pickup Form
driver.find_element(By.CSS_SELECTOR, "#pickup-form button[type='submit']").click()

# ✅ Wait for success message
success_msg = wait.until(EC.visibility_of_element_located((By.ID, "success-message")))
print("✅ Pickup request submitted! Message:", success_msg.text)

# Leave browser open for inspection
time.sleep(5)
driver.quit()
