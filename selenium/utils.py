
from selenium import webdriver
import os
import time

def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def capture_screenshot(driver, name="screenshot"):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{name}_{int(time.time())}.png")
    driver.save_screenshot(filepath)
    print(f"Screenshot saved at {filepath}")
