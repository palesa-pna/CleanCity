import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


HTML_FILE_PATH = os.path.abspath("index.html")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()

    # Open the local HTML file 
    driver.get("file:///" + HTML_FILE_PATH)
    time.sleep(2)

    # Navigate to Login
    login_link = driver.find_element(By.CSS_SELECTOR, 'a[data-page="login"]')
    login_link.click()
    time.sleep(3)

    # Fill login form 
    driver.find_element(By.ID, "login-email").send_keys("user@cleancity.com")
    driver.find_element(By.ID, "login-password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "#login-form button[type='submit']").click()
    time.sleep(5)

    # Verify Dashboard visibility ----
    dashboard_page = driver.find_element(By.ID, "dashboard-page")
    if dashboard_page.is_displayed():
        print("Login → Dashboard test PASSED")
    else:
        print("Login → Dashboard test FAILED")

   
finally:
    
    time.sleep(5)
    driver.quit()
