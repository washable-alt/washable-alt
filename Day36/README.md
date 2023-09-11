Day 36 

# Explored the different alphavantage APIs
Core Stock APIs documentation updated as of 10/9/2023
`Intraday` - occurs with a day - Extended Trading Hours - 4pm to 8am GMT +8 (4am to 8pm EST) [`Trending`]
`Daily` - `raw` (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume)
`Daily-adjusted` - `raw` (as-traded) daily open/high/low/close/volume values, adjusted_close values and historical split/dividend events of the global equity specified [`Trending`]
`Weekly` - weekly time-series of the global equity specified, covering 20+ years of historical data
`Weekly Adjusted` - takes into account of stock splits and dividends
`Monthly` - monthly time series of 20+ years of historical data
`Monthly Adjusted` - adjusted time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend)
`Quote Endpoint` - Lightweight alternative to time series APIs; it returns the latest price and volume information [`Trending`]
`Search Endpoint` - An API to retrieve symbols or companies [`Utility`]
`Global Market Status` - Returns the current market status of major trading venues for equities, forex and cryptocurrencies around the world [`Utility`]


# News API to retrieve news 
Endpoints:
`Everything`
`Top-headlines`
`sources`


Finished the normal-difficulty Stocks News Alert Project

Goal is to send a separate sms to phone number regarding the percentage difference between the previous day and the day before previous. 

API I queried was last updated on 2023-09-08, thus I have to minus three days using the timedelta from today's date. 

Webscrapping is done for the description.

![stock-news-alert-normal-project](https://github.com/washable-alt/washable-alt/assets/127829594/e8df1030-dfb8-44dd-8515-a2eb6c5e7980)
