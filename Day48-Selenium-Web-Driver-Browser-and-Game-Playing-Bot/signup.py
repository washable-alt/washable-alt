from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com")

try:
    firstName = driver.find_element(By.NAME, value="fName")
    firstName.send_keys("werwer")
    lastName = driver.find_element(By.NAME, value="lName")
    lastName.send_keys("werwer")
    email = driver.find_element(By.NAME, value="email")
    email.send_keys("werwer@sdfsdf.com")
    # Hit the return key
    signup = driver.find_element(By.TAG_NAME, value="button")
    signup.click()
except StaleElementReferenceException as e:
    # Wait for the page to refresh
    sleep(2)  
    signup = driver.find_element(By.TAG_NAME, value="button")
    signup.click()

sleep(3600)

#driver.close()
driver.quit()