from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")
driver.get("https://www.python.org")


# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}.")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# link = driver.find_element(By.CSS_SELECTOR, value=".small-widget.documentation-widget a")

# # link = driver.find_element(By.CSS_SELECTOR, value="div.small-widget:nth-child(3) > p:nth-child(3) > a:nth-child(1)")
# print(link.text)

# xpath = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# xpath = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(xpath.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# print(event_times)
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# this will print a more as well, so this solution is not what we are looking for
# for name in event_names:
#     print(name.text)

# Instead initialise an empty dictionary
events_one = {}

for i in range(len(event_times)):
    events_one[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }


events_two = {
    i: {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }for i in range(len(event_times))
}

pprint(events_one)
pprint(events_two)

store_list=['Cursor - 15', 'Grandma - 100', 'Factory - 500', 'Mine - 2,000', 'Shipment - 7,000', 'Alchemy lab - 50,000', 'Portal - 1,000,000', 'Time machine - 123,456,789']
upgrades=[['Cursor', 21], ['Grandma', 123], ['Factory', 550], ['Mine', 2000], ['Shipment', 7000], ['Alchemy lab', 50000], ['Portal', 1000000], ['Time machine', 123456789]]


money = 2000

affordable_upgrades = []

first_element_removed = False

for i in reversed(range(len(upgrades))):
    if int(upgrades[i][1]) < int(money):
        affordable_upgrades.append(upgrades[i][0])
affordable_upgrades.pop()
print(affordable_upgrades)

sleep(3600)




# driver.close()
driver.quit()