import constants
import yfinance as yf   
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup, Tag
import pprint
import re


def getPercentChange(current, previous) ->str:
    return "%.3g"%((current - previous)/previous * 100) + "%"


def getPriceChangeStr(current, open, label:str) ->str:
    diff = "+%.3g"%(current-open) if (current-open) >= 0 else "%.3g"%(current-open)
    return diff + " (" + getPercentChange(current, open) + ") "+label


def human_format(num):
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
    "Finds exchanger ending for scraping on google finance. ex result: https://www.google.com/finance/quote/MSFT:NASDAQ"
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

def scrapePrice(soup:BeautifulSoup):
    return float(re.sub("[$|,]","",soup.find("div", {"class":["YMlKec fxKbKc"]}).text))

def scrapePrevClose(soup:BeautifulSoup):
    return float(re.sub("[$|,]","",soup.find("div", {"class":"P6K39c"}).text))



def main():
    print("We out")
    data = requests.get(getScrapingURL("msft"), headers=constants.REQ_HEADER).text
    soup = BeautifulSoup(data, "lxml")
    print(scrapePrice(soup))

if __name__ == "__main__":
    main()