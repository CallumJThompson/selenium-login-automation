from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os

# 1. SETUP: Point to the manual file
# This looks for 'msedgedriver.exe' in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, "msedgedriver.exe")

driver = webdriver.Edge(service=Service(driver_path))

try:
    # 2. NAVIGATE
    print("Opening Edge...")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # 3. INTERACT
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    print("Credentials entered. Logging in...")

    # 4. CHECK RESULT
    time.sleep(2)
    success_text = driver.find_element(By.ID, "flash").text

    if "You logged into a secure area!" in success_text:
        print("TEST PASSED: Login successful.")
    else:
        print("TEST FAILED: Success message not found.")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("Closing browser...")
    driver.quit()
