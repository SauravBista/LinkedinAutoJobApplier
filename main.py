from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Credentials import MY_EMAIL, MY_PASS

# Set up Chrome options to keep the browser open after the script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to LinkedIn's homepage
driver.get("https://www.linkedin.com/")
time.sleep(3)  # Wait for the page to load

# Find and click the sign-in button
sign_in_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/a')
sign_in_button.click()

# Find the email and password input fields and enter the credentials
email = driver.find_element(By.XPATH, value='//*[@id="username"]')
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
email.send_keys(MY_EMAIL)
password.send_keys(MY_PASS)

# Submit the login form
password.send_keys(Keys.ENTER)

# Wait for the user to complete the captcha if required
input = input("Type yes after completing captcha")

# Proceed if the user confirms captcha completion
if input == "yes":
    time.sleep(4)  # Wait for the page to load after login

    # Find and click the 'Jobs' navigation link
    jobs = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
    jobs.click()
    time.sleep(3)  # Wait for the Jobs page to load

    # Find the job search input field, enter the job title, and submit the search
    input1 = driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-keyword-id-ember295"]')
    input1.send_keys("content creator intern flowrage")
    input1.send_keys(Keys.ENTER)
    time.sleep(4)  # Wait for the search results to load

    # Find and click the Easy Apply button for the first job in the results
    easy_apply = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
    easy_apply.click()
    time.sleep(2)  # Wait for the Easy Apply modal to open

    # Find and click the submit application button
    submit_application = driver.find_element(By.CSS_SELECTOR, value="footer button")
    submit_application.click()

