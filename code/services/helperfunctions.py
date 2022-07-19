import requests
import constants
import json




def isTickerValid(ticker:str) -> bool:
    data = requests.get(constants.API_URL + constants.VALIDATE_TICKER_ENDING + ticker).text
    print(data)
    return data == constants.TRUE

def getInfo(ticker:str) -> dict:
    data = requests.get(constants.API_URL + constants.GET_TICKER_INFO_ENDING + ticker).json()
    return data