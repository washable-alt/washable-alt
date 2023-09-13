import requests
from dotenv import load_dotenv
import os
from pprint import pprint
from datetime import datetime, timedelta  
from bs4 import BeautifulSoup
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#STOCK_NAME = "AAPL"
#COMPANY_NAME = "Apple"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

STOCKS_API_KEY = os.getenv("STOCKS_API_KEY")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")

AUTH_TOKEN = os.getenv("AUTH_TOKEN")

PHONE_NUMBER = os.getenv("PHONE_NUMBER")

MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_API_KEY,
}
try: 

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

    response = requests.get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    #print(response)
    data = response.json()
    #pprint(data)
    #pprint(data['Time Series (Daily)'])
    #for (stock_date, stock_price) in data['Time Series (Daily)'].items():
    #    date_format = r"%Y-%m-%d"
    #    stock_date_obj = datetime.strptime(stock_date, date_format)
    #    #print(stock_date_obj)
    #    #print(type(stock_date_obj))
    #    #print(type(stock_price['4. close']))
    #    previous_day = datetime.utcnow().date() - timedelta(days=3)
    #    previous_day_obj = datetime.strptime(previous_day.strftime(date_format), date_format)
    #    print(previous_day_obj)
    #    #print(type(previous_day_obj))
    #    day_before_previous = datetime.utcnow().date() - timedelta(days=4)
    #    day_before_previous_obj = datetime.strptime(day_before_previous.strftime(date_format), date_format)
    #    if stock_date_obj == previous_day_obj:
    #        print(stock_price['4. close'])
    #    if stock_date_obj == day_before_previous_obj:
    #        print(stock_price['4. close'])

    date_format = r"%Y-%m-%d"
    # previous day should be day minus one, remember to edit this, the api end point provided latest data is 3 days ago
    previous_date = datetime.utcnow().date() - timedelta(days=1)
    pprint(previous_date)
    #print(type(previous_date))
    ##print(previous_date)
    ##stock_date_obj = datetime.strptime(stock_date, date_format)
    #previous_date_object = datetime.strptime(previous_date.strftime(date_format), date_format)
    #pprint(f"previous date object: {previous_date_object}")
    previous_day_stock_close_price_list = [stock_price['4. close'] for (stock_date, stock_price) in data['Time Series (Daily)'].items() if datetime.strptime(stock_date, date_format).date() == previous_date]
    pprint(previous_day_stock_close_price_list)
    def get_previous_day_stock_close_price():
        for previous in previous_day_stock_close_price_list:
            return previous
    
        
#TODO 2. - Get the day before yesterday's closing stock price
    day_before_previous = datetime.utcnow().date() - timedelta(days=4)
    pprint(day_before_previous)
    # ignore this object line as this is rounded to the next day
    #day_before_previous_object = datetime.strptime(previous_date.strftime(date_format), date_format)
    #pprint(f"day_before_previous_object: {day_before_previous_object}")
    day_before_previous_stock_close_price_list = [stock_price['4. close'] for (stock_date, stock_price) in data['Time Series (Daily)'].items() if datetime.strptime(stock_date, date_format).date() == day_before_previous]
    pprint(day_before_previous_stock_close_price_list)
    def get_day_before_previous_stock_close_price():
        for day_before_previous in day_before_previous_stock_close_price_list:
            return day_before_previous

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    positive_difference_list = [abs(float(x) - float(y)) for x,y in zip(day_before_previous_stock_close_price_list,previous_day_stock_close_price_list)]
    print(positive_difference_list)
    print(type(positive_difference_list))
    def get_positive_difference():
        for positive_difference in positive_difference_list:
        #print(positive_difference)
            return positive_difference

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    def percentage_difference(a, b):
        return (float(a) - float(b)) / float(a) * 100
    day_before_previous = get_day_before_previous_stock_close_price()
    previous = get_previous_day_stock_close_price()
    percentage_diff= percentage_difference(day_before_previous, previous)
    print(percentage_diff)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    global news_parameters
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "q": COMPANY_NAME,
        "domains":"techcrunch.com"
    }
    if percentage_diff > 1:
        print('Get News')
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
        news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
        news_response.raise_for_status()
        news_data = news_response.json() 
        #print(news_data['articles'])
        #print(news_data['articles'][0:3])
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
        three_articles = news_data['articles'][:3]
#TODO 8. - Get the headline and brief       
        for dictionary in three_articles:
            print(dictionary['title'])
            title = dictionary['title']
            url = f"{dictionary['url']}"
            #print(url)
            req = requests.get(url)
            content = req.text
            #print(content)
            soup = BeautifulSoup(content, features="html.parser")
            #print(soup)
            try:
                raw = soup.find('meta', property="og:description")
                if raw:
                    meta_content = raw.get('content')


#TODO 9. - Send each article as a separate message via Twilio.                    
                    client = Client(ACCOUNT_SID, AUTH_TOKEN)
                    message = client.messages.create(
                        from_=PHONE_NUMBER,
                        to=MY_PHONE_NUMBER, 
                        body=f'{STOCK_NAME}: 🔺{abs(percentage_diff):.2f}%\nHeadline: {title}\nBrief: {meta_content}'
                        )

            except Exception as e:
                print(e)
        
    elif percentage_diff < 0:
        
        news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
        news_response.raise_for_status()
        news_data = news_response.json() 
        three_articles = news_data['articles'][:3]
        
        for dictionary in three_articles:
            print(dictionary['title'])
            title = dictionary['title']
            url = f"{dictionary['url']}"
            #print(url)
            req = requests.get(url)
            content = req.text
            #print(content)
            soup = BeautifulSoup(content, features="html.parser")
            #print(soup)
            try:
                raw = soup.find('meta', property="og:description")
                if raw:
                    meta_content = raw.get('content')
                    client = Client(ACCOUNT_SID, AUTH_TOKEN)
                    message = client.messages.create(
                        from_=PHONE_NUMBER,
                        to=MY_PHONE_NUMBER, 
                        body=f'{STOCK_NAME}: 🔻{abs(percentage_diff):.2f}%\nHeadline: {title}\nBrief: {meta_content}'
                        )

            except Exception as e:
                print(e)

except Exception as e:
    print(e)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
