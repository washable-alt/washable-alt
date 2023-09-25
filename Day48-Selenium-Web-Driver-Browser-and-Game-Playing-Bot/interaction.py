from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep


# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# print(article_count.text)
# Open to next page 
# article_count.click()

# Go to victoria
victoria = driver.find_element(By.LINK_TEXT, value="Victoria")
# victoria.click()

try:
    search = driver.find_element(By.NAME, value="search")
    search.send_keys("Python")
    # Hit the return key
    search.send_keys(Keys.ENTER)
except StaleElementReferenceException as e:
    sleep(2)  # Wait for the page to refresh
    search = driver.find_element(By.NAME, value="search")
    # Hit the return key
    search.send_keys(Keys.ENTER)

sleep(3600)

#driver.close()
driver.quit()