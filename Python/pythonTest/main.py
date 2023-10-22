from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

valid_username = os.getenv("VALID_USERNAME")
valid_password = os.getenv("VALID_PASSWORD")
invalid_username = os.getenv("INVALID_USERNAME")
invalid_password = os.getenv("INVALID_PASSWORD")

driver = webdriver.Chrome()

login_url = "https://unsplash.com/login" 

def perform_login(username, password):
    driver.get(login_url)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[email]"))
    )

    password_field = driver.find_element(By.NAME, "user[password]")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.NAME, "commit")
    login_button.click()

    if "dashboard" in driver.current_url:
        print(f"Success: Logged in as {username}")
    else:
        print(f"Failed: Unable to log in as {username}")

print("Testing Login Attempts:")
print("-----------------------")
perform_login(valid_username, valid_password)
perform_login(invalid_username, valid_password)
perform_login(valid_username, invalid_password)

driver.quit()
