import constants
import yfinance as yf   
import requests



def getTicker(company:str):
    data = requests.get(f"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={company}&callback=YAHOO.Finance.SymbolSuggest.ssCallback").json()
    result = data["ResultSet"]["Result"]
    print(result)





def main():
    print("We out")

if __name__ == "__main__":
    main()