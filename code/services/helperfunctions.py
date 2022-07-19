import yfinance as yf


def isTickerValid(ticker:str) -> bool:
    try:
        tickerObj = yf.Ticker(ticker)
        tickerObj.info["longName"]
        return True
    except:
        return False
