TRUE  = "true"
FALSE = "false"


API_URL          = "https://Foresightapi.herokuapp.com"
REQ_HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}



VALIDATE_TICKER_ENDING= "/isTickerValid/"
GET_TICKER_INFO_ENDING= "/getInfo/"
GET_NEWS_ENDING= "/getNews/"
GET_FINANCIALS_ENDING= "/getFinancials/"

EXAMPLE_INFO = {'52WeekChange': -0.08975369,
 'SandP52WeekChange': -0.11385685,
 'address1': 'One Microsoft Way',
 'algorithm': None,
 'annualHoldingsTurnover': None,
 'annualReportExpenseRatio': None,
 'ask': 259.14,
 'askSize': 1200,
 'averageDailyVolume10Day': 24772610,
 'averageVolume': 31688331,
 'averageVolume10days': 24772610,
 'beta': 0.932311,
 'beta3Year': None,
 'bid': 259.12,
 'bidSize': 900,
 'bookValue': 21.773,
 'category': None,
 'circulatingSupply': None,
 'city': 'Redmond',
 'coinMarketCapLink': None,
 'companyOfficers': [],
 'country': 'United States',
 'currency': 'USD',
 'currentPrice': 259.23,
 'currentRatio': 1.988,
 'dateShortInterest': 1656547200,
 'dayHigh': 259.59,
 'dayLow': 253.69,
 'debtToEquity': 47.863,
 'dividendRate': 2.48,
 'dividendYield': 0.0097,
 'earningsGrowth': 0.094,
 'earningsQuarterlyGrowth': 0.082,
 'ebitda': 94982995968,
 'ebitdaMargins': 0.49327,
 'enterpriseToEbitda': 19.933,
 'enterpriseToRevenue': 9.833,
 'enterpriseValue': 1893338447872,
 'exDividendDate': 1660694400,
 'exchange': 'NMS',
 'exchangeTimezoneName': 'America/New_York',
 'exchangeTimezoneShortName': 'EDT',
 'expireDate': None,
 'fiftyDayAverage': 261.1042,
 'fiftyTwoWeekHigh': 349.67,
 'fiftyTwoWeekLow': 241.51,
 'financialCurrency': 'USD',
 'fiveYearAverageReturn': None,
 'fiveYearAvgDividendYield': 1.25,
 'floatShares': 7472077634,
 'forwardEps': 10.73,
 'forwardPE': 24.159369,
 'freeCashflow': 48917000192,
 'fromCurrency': None,
 'fullTimeEmployees': 181000,
 'fundFamily': None,
 'fundInceptionDate': None,
 'gmtOffSetMilliseconds': '-14400000',
 'grossMargins': 0.6873,
 'grossProfits': 115856000000,
 'heldPercentInsiders': 0.00075,
 'heldPercentInstitutions': 0.71946996,
 'impliedSharesOutstanding': 0,
 'industry': 'Software—Infrastructure',
 'isEsgPopulated': False,
 'lastCapGain': None,
 'lastDividendDate': 1652832000,
 'lastDividendValue': 0.62,
 'lastFiscalYearEnd': 1625011200,
 'lastMarket': None,
 'lastSplitDate': 1045526400,
 'lastSplitFactor': '2:1',
 'legalType': None,
 'logo_url': 'https://logo.clearbit.com/microsoft.com',
 'longBusinessSummary': 'Microsoft Corporation develops, licenses, and '
                        'supports software, services, devices, and solutions '
                        'worldwide. Its Productivity and Business Processes '
                        'segment offers Office, Exchange, SharePoint, '
                        'Microsoft Teams, Office 365 Security and Compliance, '
                        'and Skype for Business, as well as related Client '
                        'Access Licenses (CAL); Skype, Outlook.com, OneDrive, '
                        'and LinkedIn; and Dynamics 365, a set of cloud-based '
                        'and on-premises business solutions for organizations '
                        'and enterprise divisions. Its Intelligent Cloud '
                        'segment licenses SQL, Windows Servers, Visual Studio, '
                        'System Center, and related CALs; GitHub that provides '
                        'a collaboration platform and code hosting service for '
                        'developers; and Azure, a cloud platform. It also '
                        'offers support services and Microsoft consulting '
                        'services to assist customers in developing, '
                        'deploying, and managing Microsoft server and desktop '
                        'solutions; and training and certification on '
                        'Microsoft products. Its More Personal Computing '
                        'segment provides Windows original equipment '
                        'manufacturer (OEM) licensing and other non-volume '
                        'licensing of the Windows operating system; Windows '
                        'Commercial, such as volume licensing of the Windows '
                        'operating system, Windows cloud services, and other '
                        'Windows commercial offerings; patent licensing; '
                        'Windows Internet of Things; and MSN advertising. It '
                        'also offers Surface, PC accessories, PCs, tablets, '
                        'gaming and entertainment consoles, and other devices; '
                        'Gaming, including Xbox hardware, and Xbox content and '
                        'services; video games and third-party video game '
                        'royalties; and Search, including Bing and Microsoft '
                        'advertising. It sells its products through OEMs, '
                        'distributors, and resellers; and directly through '
                        'digital marketplaces, online stores, and retail '
                        'stores. It has collaborations with Dynatrace, Inc., '
                        'Morgan Stanley, Micro Focus, WPP plc, ACI Worldwide, '
                        'Inc., and iCIMS, Inc., as well as strategic '
                        'relationships with Avaya Holdings Corp. and wejo '
                        'Limited. Microsoft Corporation was founded in 1975 '
                        'and is based in Redmond, Washington.',
 'longName': 'Microsoft Corporation',
 'market': 'us_market',
 'marketCap': 1938788974592,
 'maxAge': 1,
 'maxSupply': None,
 'messageBoardId': 'finmb_21835',
 'morningStarOverallRating': None,
 'morningStarRiskRating': None,
 'mostRecentQuarter': 1648684800,
 'navPrice': None,
 'netIncomeToCommon': 72456003584,
 'nextFiscalYearEnd': 1688083200,
 'numberOfAnalystOpinions': 46,
 'open': 257.575,
 'openInterest': None,
 'operatingCashflow': 87115997184,
 'operatingMargins': 0.42556,
 'payoutRatio': 0.2463,
 'pegRatio': 1.7,
 'phone': '425 882 8080',
 'preMarketPrice': 258,
 'previousClose': 254.25,
 'priceHint': 2,
 'priceToBook': 11.906031,
 'priceToSalesTrailing12Months': 10.068649,
 'profitMargins': 0.37627998,
 'quickRatio': 1.773,
 'quoteType': 'EQUITY',
 'recommendationKey': 'buy',
 'recommendationMean': 1.7,
 'regularMarketDayHigh': 259.59,
 'regularMarketDayLow': 253.69,
 'regularMarketOpen': 257.575,
 'regularMarketPreviousClose': 254.25,
 'regularMarketPrice': 259.23,
 'regularMarketVolume': 17378178,
 'returnOnAssets': 0.15674,
 'returnOnEquity': 0.48721,
 'revenueGrowth': 0.184,
 'revenuePerShare': 25.642,
 'revenueQuarterlyGrowth': None,
 'sector': 'Technology',
 'sharesOutstanding': 7479029760,
 'sharesPercentSharesOut': 0.0052,
 'sharesShort': 38896339,
 'sharesShortPreviousMonthDate': 1653955200,
 'sharesShortPriorMonth': 46001375,
 'shortName': 'Microsoft Corporation',
 'shortPercentOfFloat': 0.0052,
 'shortRatio': 1.3,
 'startDate': None,
 'state': 'WA',
 'strikePrice': None,
 'symbol': 'MSFT',
 'targetHighPrice': 500,
 'targetLowPrice': 251.76,
 'targetMeanPrice': 351.45,
 'targetMedianPrice': 349.5,
 'threeYearAverageReturn': None,
 'toCurrency': None,
 'totalAssets': None,
 'totalCash': 104660000768,
 'totalCashPerShare': 13.994,
 'totalDebt': 77980999680,
 'totalRevenue': 192557006848,
 'tradeable': False,
 'trailingAnnualDividendRate': 2.42,
 'trailingAnnualDividendYield': 0.009518191,
 'trailingEps': 9.58,
 'trailingPE': 27.0595,
 'trailingPegRatio': 1.7307,
 'twoHundredDayAverage': 296.8598,
 'volume': 17378178,
 'volume24Hr': None,
 'volumeAllCurrencies': None,
 'website': 'https://www.microsoft.com',
 'yield': None,
 'ytdReturn': None,
 'zip': '98052-6399'}