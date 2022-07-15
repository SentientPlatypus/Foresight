import yfinance as yf


def isTickerValid(ticker:yf.Ticker) -> bool:
    try:
        ticker.info["longName"]
        return True
    except:
        return False
