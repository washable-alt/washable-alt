#!/usr/bin/env python3
import time
from playwright.sync_api import sync_playwright
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from email.message import EmailMessage

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100


def send_email():
    try:
        load_dotenv()
        SENDER_EMAIL = os.getenv("SENDER_EMAIL")
        RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
        PASSWORD= os.getenv("PASSWORD")

        subject = "Amazon Price Checker"

        body = """
        {description} is now {price_value}! {url}
        """
        body = body.format(description=title,price_value=price,url=url)
        em = EmailMessage()
        em['From'] = SENDER_EMAIL
        em['To'] = RECEIVER_EMAIL
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(SENDER_EMAIL, PASSWORD)
            smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, em.as_string())

        print("Successful")
    except Exception as e:
        print(e)


def main():

    with sync_playwright() as p:
        # unix timestamp
        t0 = time.time()
        # just so you know how to get it headfull for debugging
        # create without A GUI browser
        browser = p.chromium.launch(headless=False, slow_mo=50) 
        page = browser.new_page()
        page.goto(url)
        global title
        title = page.title()
        #print(page.title())
        # XPath Selector
        # Change button name based on size or style
        # page.get_by_role("button", name="8QT").highlight()
        # button = page.get_by_role("button", name="8QT").first
        # button.click()
        # Delay 5 seconds
        # time.sleep(5)

        price_locate = page.locator("(//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[@class='a-offscreen'])[1]").text_content()
        print(f"{price_locate} in {time.time()-t0:.2f}sec")
        #do not close browser in full mode for debug
        page.pause() 
        browser.close()
    global price
    price = float(price_locate.split('$')[1])
    try:
        if price < TARGET_PRICE: 
            send_email()
    except Exception as e:
        print(e)
        
if __name__=="__main__":
    main()