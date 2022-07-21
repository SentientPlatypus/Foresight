from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import requests
import yfinance as yf
import constants
import csv
from stockFunctions import human_format, getPercentChange

context = ssl.create_default_context()

def createApp():
    app = Flask(
    __name__,
    template_folder=r"templates",
    static_folder=r"static"
    )
    return app

app = createApp()


@app.route("/isTickerValid/<string:ticker>")
def isTickerValid(ticker:str) -> bool:
    """Checks if ticker is valid."""
    try:
        tickerObj = yf.Ticker(ticker)
        tickerObj.info["longName"]
        return constants.TRUE
    except:
        return constants.FALSE

@app.route("/getInfo/<string:ticker>")
def getInfo(ticker:str) -> dict:
    """Prerequisite is that ticker must be valid. Use isTickerValid for this."""
    tickerObj = yf.Ticker(ticker)
    tickerObjInfo = tickerObj.info
    
    info_we_need = {
        "companyName" : ("'" + tickerObjInfo["longName"] + "'"),
        "currentValue" : {
            "value" : str(tickerObjInfo["currentPrice"])+ "USD",
            "change" : "+6.78 (2.41%) Today"
        },
        "marketStatus" : "Closed April 22, 7:59PM EST",
        "companyDesc" : tickerObjInfo["longBusinessSummary"],
        "companyLogoUrl" : tickerObjInfo["logo_url"],
        "totalRevenue": {
            "value":human_format(tickerObjInfo["totalRevenue"]),
            "change": "+18.35%"
        },
        "revenuePerShare" : {
            "value":human_format(tickerObjInfo["revenuePerShare"]),
            "change":"+13.7%"
        },
        "ebitda" : {
            "value":human_format(tickerObjInfo["ebitda"]),
            "change":"+20.78%"
        },
        "expense" : {
            "value": human_format(tickerObjInfo["totalRevenue"] - tickerObjInfo["netIncomeToCommon"]),
            "change": "+15.22%"
        },
        "netIncome" : {
            "value":human_format(tickerObjInfo["netIncomeToCommon"]),
            "change": "+8.22"
        },
        "effectiveTaxRate" : {
            "value":"17.15%",
            "change": "-"
        }
    }
    return info_we_need

















@app.route("/")
def home():
    return {"stocks":0, "maidens":0}

def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    keep_alive()

