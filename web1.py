from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify your Naukri username and password
naukri_username = "yehovadenial@gmail.com"
naukri_password = "Daniel2456@"

# Set the path to the EdgeDriver executable
edge_driver_path = "C:\\Users\\SURENDRAN\\eclipse-workspace\\SeleniumDay2\\Driver\\msedgedriver.exe"

# Initialize the Edge WebDriver
driver = webdriver.Edge(executable_path=edge_driver_path)

try:
    # Navigate to the Naukri login page
    driver.get("https://www.naukri.com/nlogin/login")

    # To maximize the window
    driver.maximize_window()

    # Find the username and password input fields and login button
    time.sleep(3)
    username_field = driver.find_element(By.ID, "usernameField")
    password_field = driver.find_element(By.ID, "passwordField")
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

    # Enter your username and password, then click the login button
    username_field.send_keys(naukri_username)
    password_field.send_keys(naukri_password)
    login_button.click()

    # Navigate to the "View Profile" page
    time.sleep(5)
    view_profile_button = driver.find_element(By.XPATH, "//a[text()='View']")
    view_profile_button.click()

    # Find the "Summary" field and update it with your new summary
    time.sleep(3)
    profile_summary = driver.find_element(By.XPATH, "(//span[text()='Profile summary'])[1]")
    profile_summary.click()

    time.sleep(3)
    edit_summary_button = driver.find_element(By.XPATH, "(//span[text()='editOneTheme'])[20]")
    edit_summary_button.click()

    time.sleep(5)
    summary_field = driver.find_element(By.ID, "profileSummaryTxt")
    summary_field.clear()
    time.sleep(4)

    updated_summary_text = "Your updated summary text goes here"
    summary_field.send_keys(updated_summary_text)

    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
    save_button.click()

    print("Success")

finally:
    # Close the browser
    driver.quit()
