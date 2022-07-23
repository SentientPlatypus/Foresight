from turtle import getscreen
import constants
import yfinance as yf   
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup, Tag
import pprint
import re


def getPercentChange(current, previous) ->str:
    """percent difference. Example:\n
    >>> getPriceChangeStr(12, 10))\n
    >>> '20.0%'"""
    return "%.3g"%((current - previous)/previous * 100) + "%"


def getPriceChangeStr(current, open, label:str) ->str:
    """Gves string that shows difference, and percent difference along wth a label.. Example:\n
    >>> getPriceChangeStr(12, 10, 'difference'))\n
    >>> '+2.00 (20.0%) difference'"""
    diff = "+%.3g"%(current-open) if (current-open) >= 0 else "%.3g"%(current-open)
    return diff + " (" + getPercentChange(current, open) + ") "+label


def scrapeTickerFromUrl(url:str) ->str:
    """Scrapes the ticker part from the Url. For example:\n
    >>> scrapeTickerFromUrl('https://www.google.com/finance/quote/GOOGL:NASDAQ')\n
    >>> 'GOOGL'"""

def human_format(num):
    """Gives numbers human format. Example:\n
    >>> human_format(272900238)\n
    >>> '273M'"""
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


def scrapeMarketStatus(soup:BeautifulSoup) ->str:
    "Scrapes google finance page for the close and open date."
    return re.sub("Disclaimer$", "", soup.find('div', {"class":"ygUjEc","jsname":"Vebqub"}).text)

def scrapeCompanyName(soup:BeautifulSoup) ->str:
    "Scrapes google finance page for the close and open date."
    return re.sub("Disclaimer$", "", soup.find('div', {"class":"zzDege"}).text)
  

def getScrapingURL(ticker:str)->str:
    """Finds exchanger ending for scraping on google finance. Example:\n 
    >>> getScrapingURL('MSFT')
    >>> https://www.google.com/finance/quote/MSFT:NASDAQ"""
    data = requests.get(f'{constants.GOOGLE_FINANCE_URL}{ticker}', headers=constants.REQ_HEADER).text
    soup = BeautifulSoup(data, 'lxml')
    parentList = soup.find("ul", {"class":["sbnBtf xJvDsc ANokyb"]})
    url = parentList.find("a")["href"] ##finds the first option link, and retuns it.
    exchanger = url[url.index(":") + 1:]
    return f"{constants.GOOGLE_FINANCE_URL}{ticker}:{exchanger}"


def scrapeNews(soup:BeautifulSoup) -> dict:
    """Scrapes the news articles off of {constants.GOOGLE_FINANCE_URL}{ticker} in the form of a dictionary
    EXAPMLE:
    {'articles': [{'date': '18 hours ago',
               'link': 'https://www.cnbc.com/2022/07/20/microsoft-eases-up-on-hiring-as-economic-concerns-hit-more-of-the-tech-industry.html',
               'publisher': 'CNBC',
               'title': 'Microsoft eases up on hiring as economic concerns hit '
                        'more of the tech \n'
                        'industry'},
              {'date': '2 days ago',
               'link': 'https://www.barrons.com/articles/microsoft-stock-recession-analyst-price-target-51658230843',
               'publisher': "Barron's",
               'title': "Microsoft Stock Is a 'Good Place to Hide.' This "
                        'Analyst CutsPrice Target \n'
                        'Anyway.'},
              {'date': '18 hours ago',
               'link': 'https://www.bloomberg.com/news/articles/2022-07-20/microsoft-cuts-many-open-job-listings-in-weakening-economy',
               'publisher': 'Bloomberg.com',
               'title': 'Microsoft Cuts Many Open Job Listings in Weakening '
                        'Economy'},
              {'date': '16 hours ago',
               'link': 'https://money.usnews.com/investing/news/articles/2022-07-20/microsoft-teams-down-for-thousands-of-users-downdetector',
               'publisher': 'US News Money',
               'title': 'Microsoft Teams Back up for Most Users After Global '
                        'Outage'},
              {'date': '1 week ago',
               'link': 'https://seekingalpha.com/article/4523194-microsoft-buy-before-q4-earnings',
               'publisher': 'Seeking Alpha',
               'title': 'Microsoft Stock: A Buy Before Q4 Earnings '
                        '(NASDAQ:MSFT)'},
              {'date': '20 hours ago',
               'link': 'https://www.tipranks.com/news/article/microsoft-stock-fx-headwinds-likely-to-persist-says-analyst/',
               'publisher': 'TipRanks',
               'title': 'Microsoft Stock: FX Headwinds Likely to Persist, Says '
                        'Analyst'},
              {'date': '1 day ago',
               'link': 'https://finbold.com/citi-analyst-views-microsoft-as-a-solid-recession-proof-stock/',
               'publisher': 'Finbold',
               'title': 'Citi analyst views Microsoft as a solid '
                        'recession-proof stock'}]}"""
    newsBoxes = soup.find_all("div", {"class":["zLrlHb EA7tRd"]})
    articles = []
    if newsBoxes:
        for element in newsBoxes:
            article = {}
            article["link"] = element.find("a")["href"]
            article["publisher"] = element.find("div", {"class":"AYBNIb"}).text
            article["date"] = re.sub("\n","",element.find("div", {"class":"HzW5e"}).text)
            article["title"] = element.find("div", {"class":"F2KAFc"}).text
            articles.append(article)
        return {"articles":articles}
    else:
        newsBoxes = soup.find_all("div", {"class":"yY3Lee"})
        for element in newsBoxes:
            article = {}
            article["link"] = element.find("a")["href"]
            article["publisher"] = element.find("div", {"class":"sfyJob"}).text
            article["date"] = re.sub("\n","",element.find("div", {"class":"Adak"}).text)
            article["title"] = element.find("div", {"class":"Yfwt5"}).text
            articles.append(article)
        return {"articles":articles}


def scrapeCompanyDesc(soup:BeautifulSoup) ->str:
    return re.sub("\. Wikipedia$","",soup.find("div", {"class":"bLLb2d"}).text)

def getFloat(num:str) ->float:
    """Returns the float of a number containing symbols
    >>> getFloat('$262.27')
    >>> 262.27"""
    return float(re.sub("[$,]", "", num))

def scrapePrice(soup:BeautifulSoup):
    return soup.find("div", {"class":["YMlKec fxKbKc"]}).text

def scrapePrevClose(soup:BeautifulSoup):
    return soup.find("div", {"class":"P6K39c"}).text

def scrapeIncomeStatement(soup:BeautifulSoup) ->dict:
    """current keys:\n
Revenue\n
Operating expense\n
Net income\n
Net profit margin\n
Earnings per share\n
EBITDA\n
Effective tax rate"""
    incomeStatement = {}
    incomeStatementTable = soup.find_all("table", {"class":"slpEwd"})[constants.INCOME_STATEMENT_INDEX]
    rows = incomeStatementTable.find_all("tr", {"class":"roXhBd"})[1:]
    for row in rows:
        label = row.find("div", {"class":"rsPbEe"}).text
        value = row.find("td", {"class":"QXDnM"}).text
        try:
            yearChange = row.find("span",{"class":["JwB6zf", "CnzlGc"]}).text
        except:
            yearChange = row.find("td",{"class":"gEUVJe"}).text
        if yearChange[0] not in ["—", "-"]:
            yearChange = "+" + yearChange
        incomeStatement[label] = {"value":value, "change":yearChange}
    return incomeStatement

def scrapeBalanceSheet(soup:BeautifulSoup) ->dict:
    """current keys:\n
Cash and short-term investments\n
Total assets\n
Total liabilities\n
Total equity\n
Shares outstanding\n
Price to book\n
Return on assets\n
Return on capital"""
    balanceSheet = {}
    balanceSheetTable = soup.find_all("table", {"class":"slpEwd"})[constants.BALANCE_SHEET_INDEX]
    rows = balanceSheetTable.find_all("tr", {"class":"roXhBd"})[1:]
    for row in rows:
        label = row.find("div", {"class":"rsPbEe"}).text
        value = row.find("td", {"class":"QXDnM"}).text
        try:
            yearChange = row.find("span",{"class":["JwB6zf", "CnzlGc"]}).text
        except:
            yearChange = row.find("td",{"class":"gEUVJe"}).text
        if yearChange[0] not in ["—", "-"]:
            yearChange = "+" + yearChange
        balanceSheet[label] = {"value":value, "change":yearChange}
    return balanceSheet

def scrapeCashFlow(soup:BeautifulSoup) ->dict:
    """current keys:\n
Net income\n
Cash from operations\n
Cash from investing\n
Cash from financing\n
Net change in cash\n
Free cash flow"""
    CashFlow = {}
    CashFlowTable = soup.find_all("table", {"class":"slpEwd"})[constants.CASH_FLOW_INDEX]
    rows = CashFlowTable.find_all("tr", {"class":"roXhBd"})[1:]
    for row in rows:
        label = row.find("div", {"class":"rsPbEe"}).text
        value = row.find("td", {"class":"QXDnM"}).text
        try:
            yearChange = row.find("span",{"class":["JwB6zf", "CnzlGc"]}).text
        except:
            yearChange = row.find("td",{"class":"gEUVJe"}).text
        if yearChange[0] not in ["—", "-"]:
            yearChange = "+" + yearChange
        CashFlow[label] = {"value":value, "change":yearChange}
    return CashFlow

def scrapeCompanyWebsite(soup:BeautifulSoup) ->str:
    "Returns the URL for the company website"
    container = soup.find("div", {"class":"v5gaBd Yickn"})
    rows = container.find_all("div", {"class":"gyFHrc"})
    for row in rows:
        try:
            if row.find("div", {"class":"mfs7Fc"}).text == "Website":
                return row.find("a", {"class":"tBHE4e"})["href"]
        except:
            pass
    return "NO URL"

def scrapeCompanyLogo(companyWebsite:str):
    "Returns link to company logo given company website url"
    return constants.LOGO_CLEARBIT_URL + companyWebsite



def main():
    print(getScrapingURL("msft"))
    print("We out")
    data = requests.get(getScrapingURL("msft"), headers=constants.REQ_HEADER).text
    soup = BeautifulSoup(data, "lxml")
    print(scrapeIncomeStatement(soup))
    # pprint.pprint(scrapeCompanyLogo(scrapeCompanyWebsite(soup)))

if __name__ == "__main__":
    main()