from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import requests
import yfinance as yf
import csv
context = ssl.create_default_context()

def createApp():
    app = Flask(
    __name__,
    template_folder=r"templates",
    static_folder=r"static"
    )
    return app

app = createApp()



# def getTicker (company_name):
#     try:
#         company = yf.Ticker(company_name)
#         information = company.info
#         longName = information["longName"]
#         return information
#     except:
#         return "invalidTicker"
#     # url = "https://s.yimg.com/aq/autoc"
#     # parameters = {'query': company_name, 'lang': 'en-US'}
#     # response = requests.get(url = url, params = parameters)
#     # data = response.json()
#     # company_code = data['ResultSet']['Result'][0]['symbol']
#     # return company_code


@app.route("/checkTicker/<string:companyName>")
def checkTicker(companyName:str):
    try:
        company = yf.Ticker(companyName)
        information = company.info
        longName = information["longName"]
        return information
    except:
        return "invalidTicker"

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

