import requests

API_KEY = "2XQWGIM3M8AON3C9" #"42TH2SSV4WG6W1KI"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
   # "outputsize": "compact",
    #"datatype": "json",
    "apikey": API_KEY,
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params = parameters)
response.raise_for_status()
data = response.json()


#print(data)
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
view = data["Time Series (Daily)"]['2023-04-17']["4. close"]
#view = int(view)
print(view)
#TODO 2. - Get the day before yesterday's closing stock price
view_day_b_4_yesterday = data["Time Series (Daily)"]['2023-04-14']["4. close"]
viewb4y = view_day_b_4_yesterday
print(viewb4y)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
posdiff = abs(187.04 - 185)
print(posdiff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percdif = (posdiff/((187.04 + 185)/2)) * 100
percdif = round(percdif, 3)
print(percdif)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
API_KEY_NEWS = "fa16e83aae5e46a2a78b14fcb0ccfece"
#newsapi = NewsApiClient(api_key= API_KEY_NEWS)
param = {
    "q": COMPANY_NAME,
    "from": '2023-04-17',
    "apikey": API_KEY_NEWS,
    "sortBy": "popularity",
}


response1 = requests.get(NEWS_ENDPOINT, params= param)
response1.raise_for_status()
data_news = response1.json()
print(data_news)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



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

