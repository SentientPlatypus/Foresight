import constants
import yfinance as yf   
import requests
import pandas as pd
from googlefinance import getQuotes
import json

def getPercentChange(current, previous) ->str:
    return "%.3g"%((current - previous)/previous * 100) + "%"

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

data = json.dumps(getQuotes('AAPL'), indent=2)

print("data")



def main():
    print("We out")

if __name__ == "__main__":
    main()