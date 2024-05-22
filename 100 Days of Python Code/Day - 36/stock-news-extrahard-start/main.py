import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = os.environ["API_KEY_STOCK"]
API_KEY_NEWS = os.environ["API_KEY_NEWS"]
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"5min",
    "apikey":API_KEY_STOCK
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
Yesterday = data_list[0]
Day_Before_Yesterday = data_list[1]
Yesterday_price = float(Yesterday["4. close"])
Day_Before_Yesterday_price = float(Day_Before_Yesterday["4. close"])
percent = ((Yesterday_price-Day_Before_Yesterday_price) / Yesterday_price) * 100

def news():
    parameters2 = {
        "q":"tesla",
        "from":"2024-03-08",
        "sortBy":"publishedAt",
        "apiKey": API_KEY_NEWS,
        "language":"en"
    }
    response2 = requests.get(url="https://newsapi.org/v2/everything", params=parameters2)
    response2.raise_for_status()
    news_data = response2.json()
    for i in range(3):
        title = (news_data["articles"][i]["title"])
        brief = news_data["articles"][i]["description"]

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"TSLA: {round(percent,2)}%\nHeadlines: {title}\nBrief: {brief}",
            from_='+16562184044',
            to='+yournumber'
        )
        print(message.status)


if -5>percent or 5<percent:
    print("News")
    news()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

