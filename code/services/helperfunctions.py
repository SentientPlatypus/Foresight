import requests
import constants
import json




def isTickerValid(ticker:str) -> bool:
    data = requests.get(constants.API_URL + constants.VALIDATE_TICKER_ENDING + ticker).text
    print(data)
    return data == constants.TRUE

print(isTickerValid("msft"))

def getInfo(ticker:str) -> dict:
    data = requests.get(constants.API_URL + constants.GET_TICKER_INFO_ENDING + ticker).json()
    return data

def getNews(ticker:str) ->list[dict]:
    data = requests.get(constants.API_URL + constants.GET_NEWS_ENDING + ticker).json()
    return data

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])




def getPercentChange(current, previous) ->str:
    return str((current - previous)/previous * 100) + "%"