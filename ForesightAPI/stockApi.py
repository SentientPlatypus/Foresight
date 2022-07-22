from gettext import find
from tkinter import EW
from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import requests
from sqlalchemy import true
import yfinance as yf
import constants
import csv
from bs4 import BeautifulSoup
from scraper import *

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
def isTickerValid(ticker:str) -> str:
    """Checks if ticker is valid."""
    data = requests.get(f"{constants.GOOGLE_FINANCE_URL}{ticker}").text
    soup = BeautifulSoup(data, "lxml")
    if soup.find("ul", {"class":constants.OPTIONS_LIST_CLASSES}):
        return constants.TRUE
    else:
        return constants.TRUE if soup.find("div", {"class":"zzDege"}) else constants.FALSE

@app.route("/getInfo/<string:ticker>")
def getInfo(ticker:str) -> dict:
    """Prerequisite is that ticker must be valid. Use isTickerValid for this."""
    tickerObj = yf.Ticker(ticker)
    tickerObjInfo = tickerObj.info

    scrapingURL = getScrapingURL(ticker)
    data = requests.get(scrapingURL, headers=constants.REQ_HEADER).text
    soup = BeautifulSoup(data, "lxml")
    
    info_we_need = {
        "companyName" : scrapeCompanyName(soup),
        "currentValue" : {
            "value" : scrapePrice(soup),
            "change" : getPriceChangeStr(scrapePrice(soup), scrapePrevClose(soup), "Today")
        },
        "marketStatus" : scrapeMarketStatus(soup),
        "companyDesc" : scrapeCompanyDesc(soup),
        "companyLogoUrl" : tickerObjInfo["logo_url"]
    }
    return info_we_need

@app.route("/getFinancials/<string:ticker>")
def getFinancials(ticker:str) -> dict:
    scrapingURL = getScrapingURL(ticker)
    data = requests.get(scrapingURL, headers=constants.REQ_HEADER).text
    soup = BeautifulSoup(data, "lxml")
    financials = {
        "incomeStatement": scrapeIncomeStatement(soup),
        "balanceSheet":scrapeBalanceSheet(soup),
        "cashFlow":scrapeCashFlow(soup)
    }
    return financials


@app.route("/getNews/<string:ticker>")
def getNews(ticker:str) -> dict:
    return scrapeNews(getScrapingURL(ticker))

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

