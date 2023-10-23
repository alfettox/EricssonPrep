from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

valid_username = "tomsmith"
valid_password = "SuperSecretPassword!"
invalid_username = "USERNAME"
invalid_password = "PASSWORD"

driver = webdriver.Chrome()

login_url = "https://opensource-demo.orangehrm.com/"


def perform_login(username, password):
    driver.get(login_url)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'user-name')))
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.submit()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'inventory_container')))
    result = driver.page_source
    print(result)
    print("-----------------------")




print("Testing Login Attempts:")
print("Valid Username:", valid_username)
print("Valid Password:", valid_password)
print("-----------------------")
perform_login(valid_username, valid_password)
perform_login(invalid_username, valid_password)
perform_login(valid_username, invalid_password)

driver.quit()
