import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

import time
import datetime
import re
import math

# init variables:

# time:
main_end_time = time.time() + 60 * 5
seconds_to_run = 5

# Starting Prices:
cursor_price = 15
grandma_price = 100
factory_price = 500
mine_price = 2000
shipment_price = 7000
alchemy_lab_price = 50000

# My Possessions:
my_cursors = 0
my_grandmas = 0
my_factories = 0
my_mines= 0
my_shipments = 0
my_alchemy_labs = 0

def cookie_click():
    myloop = 0
    exec_end_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds_to_run)
    while True:
        myloop += 1
        if datetime.datetime.now() >= exec_end_time:
            # temp
            print(f"{seconds_to_run} seconds ended") 
            # temp
            time.sleep(1) 
            break
        mycookie.click()

def buy_addons():
    global factory_price, shipment_price, mine_price, grandma_price, cursor_price, alchemy_lab_price
    global my_cursors, my_grandmas, my_factories, my_mines, my_shipments, my_alchemy_labs
    mymoney = int(re.sub(",", "", money.text))
    print(f'money on hand:{mymoney}$, checkin for stuff to buy')
    if mymoney >= alchemy_lab_price:
        while mymoney >= alchemy_lab_price:
            # temp
            print('will try buying an Alchemy Lab!') 
            try:
                alchemy_lab = driver.find_element(By.ID, 'buyAlchemy lab')
                alchemy_lab.click()
                # temp
                print('...bought an Alchemy Lab!') 
                my_alchemy_labs += 1
                mymoney -= alchemy_lab_price
                alchemy_lab_price = math.ceil(alchemy_lab_price + (alchemy_lab_price * 10/100))
                # temp
                print(f"New Alchemy Lab price: ${alchemy_lab_price}")  
            except StaleElementReferenceException:
                break
    if mymoney >= shipment_price:
        while mymoney >= shipment_price:
            # temp
            print('will try buying a Shipment!') 
            try:
                shipment = driver.find_element(By.ID, 'buyShipment')
                shipment.click()
                # temp
                print('...bought a Shipment!') 
                my_shipments += 1
                mymoney -= shipment_price
                shipment_price = math.ceil(shipment_price + (shipment_price * 10/100))
                # temp
                print(f"New Shipment price: ${shipment_price}")  
            except selenium.common.exceptions.StaleElementReferenceException:
                break
    if mymoney >= mine_price:
        while mymoney >= mine_price:
            # temp
            print('will try buying a Mine!') 
            try:
                mine = driver.find_element(By.ID, 'buyMine')
                mine.click()
                # temp
                print('...bought a Mine!')
                my_mines += 1
                mymoney -= mine_price
                mine_price = math.ceil(mine_price + (mine_price * 10/100))
                # temp
                print(f"New mine price: ${mine_price}")  
            except StaleElementReferenceException:
                break
    if mymoney >= factory_price:
        while mymoney >= factory_price:
            # temp
            print('will try buying a Factory!') 
            # temp
            time.sleep(1)  
            try:
                factory = driver.find_element(By.ID, 'buyFactory')
                # temp
                print(factory.text) 
                factory.click()
                # temp
                print('...bought a Factory!') 
                my_factories += 1
                mymoney -= factory_price
                factory_price = math.ceil(factory_price + (factory_price * 10/100))
                # temp
                print(f"New factory price: ${factory_price}")  
            except StaleElementReferenceException:
                break
    if mymoney >= grandma_price:
        while mymoney >= grandma_price:
            # temp
            print('will try buying a Grandma!') 
            try:
                grandma = driver.find_element(By.ID, 'buyGrandma')
                grandma.click()
                # temp
                print('...bought a Grandma!') 
                my_grandmas += 1
                mymoney -= grandma_price
                grandma_price = math.ceil(grandma_price + (grandma_price * 10/100))
                # temp
                print(f"New grandma price: ${grandma_price}")  
            except StaleElementReferenceException:
                break
    if mymoney >= cursor_price:
        while mymoney >= cursor_price:
            #temp
            print('will try buying a Cursor!') 
            try:
                cursor = driver.find_element(By.ID, 'buyCursor')
                cursor.click()
                # temp
                print('...bought a Cursor!') 
                my_cursors += 1
                mymoney -= cursor_price
                cursor_price = math.ceil(cursor_price * (cursor_price * 10/100))
                # temp
                print(f"New cursor price: ${cursor_price}")  
            except StaleElementReferenceException:
                break
    # temp
    time.sleep(1) 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/") 


mycookie = driver.find_element(By.ID, 'cookie') 
money = driver.find_element(By.ID, 'money')

# main program loop:
while time.time() < main_end_time:
    # runs for 5 seconds
    cookie_click()  
    # checks for affordable add-ons and buys most expensive(s) one(s)
    buy_addons()  

# print final CPS report
my_cookies_per_second = driver.find_element(By.ID, 'cps')
print("CPS:", my_cookies_per_second.text)
print(f"My Alchemy Labs: {my_alchemy_labs}")
print(f"My Shipments: {my_shipments}")
print(f"My Mines: {my_mines}")
print(f"My Factories: {my_factories}")
print(f"My GrandMas: {my_grandmas}")
print(f"My Cursors: {my_cursors}")



time.sleep(10)

# close browser window and quit:
driver.quit()
