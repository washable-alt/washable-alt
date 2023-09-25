from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from time import sleep, time


def cps():
    cps = driver.find_element(By.CSS_SELECTOR, value="#cps").text
    return cps

def buy_item(upgrade):
    buy_item = driver.find_element(By.ID, value='buy'+ upgrade[0].strip())
    #print(buy_item.text)
    try:
        buy_item.click()   
    except NoSuchElementException:
        sleep(0.01)
        buy_item.click()
    except StaleElementReferenceException:
        print("Cursor not there anymore!")


def check_money():
    current_money = driver.find_element(By.CSS_SELECTOR, value="#money").text
    if "," in current_money:
            current_money = current_money.replace(",", "")
    return current_money

def check_store():
    # store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    
    # store_list = []
    # for item in store_items:
    #     print(item.text)
    #     store_list.append(item.text)
    # print(store_list)
    
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    # pop removes the last element of the list
    store_items.pop()
    store_list = [item.text for item in store_items]
    #print(store_list)
    upgrades = []
    for item in store_items:
        upgrades.append([
            item.text.split('-')[0].strip(),
            int((item.text.split('-')[1].replace(',','')))
        ])
    #print(upgrades)
    money = int(check_money())
    #print(money)
    first_element_removed = False
    second_element_removed = False
    third_element_removed = False

    for i in reversed(range(len(upgrades))):
        if money >= upgrades[i][1]:
            try:
                if time() > half_min:
                    if not first_element_removed:
                        upgrades.pop(0)
                        first_element_removed=True
                    buy_item(upgrades[i])
                    print(upgrades)
                if time() > one_min:
                    if not second_element_removed:
                        upgrades.pop(0)
                        second_element_removed=True
                    print(upgrades)
                    buy_item(upgrades[i])
                if time() > two_min:
                    if not third_element_removed:
                        upgrades.pop(0)
                        second_element_removed=True
                    print(upgrades)
                    buy_item(upgrades[i])
                if time() < one_min:
                    # buy all possible upgrades
                    buy_item(upgrades[i])
                    print(upgrades)

            except StaleElementReferenceException as e:
                sleep(0.01)
                if time() > half_min:
                    if not first_element_removed:
                        upgrades.pop(0)
                        first_element_removed=True
                    buy_item(upgrades[i])
                    print(upgrades)
                if time() > one_min:
                    if not second_element_removed:
                        upgrades.pop(0)
                        second_element_removed=True
                    print(upgrades)
                    buy_item(upgrades[i])
                if time() > two_min:
                    if not third_element_removed:
                        upgrades.pop(0)
                        second_element_removed=True
                    print(upgrades)
                    buy_item(upgrades[i])
                if time() < one_min:
                    # buy all possible upgrades
                    buy_item(upgrades[i])
                    print(upgrades)
            
def main():
     # Keep Chrome browser open after the program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    global driver, cps, half_min, one_min, two_min, five_min, timeout
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://orteil.dashnet.org/experiments/cookie/")
    # driver.get("https://orteil.dashnet.org/cookieclicker/")
    cookie = driver.find_element(By.ID, 'cookie')
    
    
    timeout = time() + 1


    # half minute later
    half_min = time() + 30

    # one minute later
    one_min = time() + 60

    # two minute later
    two_min = time() + 60*2

    # 5 minutes later
    five_min = time() + 60*5
    
    while True:
        cookie.click()
        if time() > timeout :
            check_store()
            timeout += 10
            cookies_per_second = cps()
            print(cookies_per_second)
        if time() > five_min:
            timeout += 10
            cookies_per_second = cps()
            print(cookies_per_second)
            driver.quit()
    #driver.close()
    #driver.quit()

if __name__=="__main__":
    main()