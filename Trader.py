import time
import re
import requests
import trading212api
import random
from io import StringIO
from datetime import datetime, timedelta
import bs4
from bs4 import BeautifulSoup
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


while True:
	print("Welcome to algorithmic trader")
	time.sleep(2)
	print("Would you like me to begin trading?")
	permission_input = input("(yes/no):\n")
	

	if permission_input == "no":
		print("You entered:", permission_input)
		time.sleep(2)
		print("Okay, another time then. Goodbye")
		break

	elif permission_input == "yes":
		print("You entered:", permission_input)
		time.sleep(2)
		print("Okay! I am going to begin, press cntrl + c to exit at any time")
		time.sleep(1)
		print("Beginning my research phase")
		
		while True :

			class YahooFinanceHistory:
   			 	timeout = 2
   				crumb_link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    			crumble_regex = r'CrumbStore":{"crumb":"(.*?)"}'
    			quote_link = 'https://query1.finance.yahoo.com/v7/finance/download/{quote}?period1={dfrom}&period2={dto}&interval=1d&events=history&crumb={crumb}'
    		def __init__(self, symbol, days_back=7):
        		self.symbol = symbol
        		self.session = requests.Session()
        		self.dt = timedelta(days=days_back)
    		def get_crumb(self):
        		response = self.session.get(self.crumb_link.format(self.symbol), timeout=self.timeout)
        		response.raise_for_status()
        		match = re.search(self.crumble_regex, response.text)
        		if not match:
            		raise ValueError('Could not get crumb from Yahoo Finance')
        		else:
            		self.crumb = match.group(1)

    		def get_quote(self):
        		if not hasattr(self, 'crumb') or len(self.session.cookies) == 0:
            	self.get_crumb()
        		now = datetime.utcnow()
        		dateto = int(now.timestamp())
        		datefrom = int((now - self.dt).timestamp())
        		url = self.quote_link.format(quote=self.symbol, dfrom=datefrom, dto=dateto, crumb=self.crumb)
        		response = self.session.get(url)
        		response.raise_for_status()
        		return pd.read_csv(StringIO(response.text), parse_dates=['Date'])

			dfAPPL = YahooFinanceHistory('AAPL', days_back=100).get_quote()
			
			dfAPPLopen = dfAPPL[['Date', 'Open']]
			dfAPPLclose = dfAPPL[['Date', 'Close']]
			
			while True:
				if:
					 
				else:
					print("The stock will not ")


			print("Finished!")
			break

	else :
		print("Error: Incorrect Input")
		break






