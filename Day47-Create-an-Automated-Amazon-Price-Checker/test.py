import time
from playwright.sync_api import sync_playwright

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

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

        # Selecting a button by XPath selector
        # Selecting the button using XPath selector
        # Select it based on the size
        page.get_by_role("button", name="8QT").highlight()
        button = page.get_by_role("button", name="8QT").first
        button.click()
        # Delay 5 seconds
        time.sleep(5)

        price_locate = page.locator("(//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']/span[@class='a-offscreen'])[1]").text_content()
        print(f"{price_locate} in {time.time()-t0:.2f}sec")
        #do not close browser in full mode for debug
        page.pause() 
        browser.close()