from application_tkinter import GUIApplication

# Pour la partie dynamique avec l'API google
class cours_index:
  def __init__(self, myapp):
    self.myapp = GUIApplication()
    pass    
     

""" from googlefinance import getQuotes
import json

from urllib.request import urlopen

print (json.dumps(getQuotes('AAPL'), indent=2))
[
  {
    "Index": "NASDAQ",
    "LastTradeWithCurrency": "129.09",
    "LastTradeDateTime": "2015-03-02T16:04:29Z",
    "LastTradePrice": "129.09",
    "Yield": "1.46",
    "LastTradeTime": "4:04PM EST",
    "LastTradeDateTimeLong": "Mar 2, 4:04PM EST",
    "Dividend": "0.47",
    "StockSymbol": "AAPL",
    "ID": "22144"
  }
]
print (json.dumps(getQuotes(['AAPL', 'VIE:BKS']), indent=2))
[
  {
    "Index": "NASDAQ",
    "LastTradeWithCurrency": "129.36",
    "LastTradeDateTime": "2015-03-03T16:02:36Z",
    "LastTradePrice": "129.36",
    "LastTradeTime": "4:02PM EST",
    "LastTradeDateTimeLong": "Mar 3, 4:02PM EST",
    "StockSymbol": "AAPL",
    "ID": "22144"
  },
  {
    "Index": "VIE",
    "LastTradeWithCurrency": "17.10",
    "LastTradeDateTime": "2015-03-03T13:30:30Z",
    "LastTradePrice": "17.10",
    "LastTradeTime": "1:30PM GMT+1",
    "LastTradeDateTimeLong": "Mar 3, 1:30PM GMT+1",
    "StockSymbol": "BKS",
    "ID": "978541942832888"
  }
]

"""