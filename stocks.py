#import numpy as np
#from sklearn.linear_model import LinearRegression
#from sklearn import preprocessing, svm
#from sklearn.model_selection import train_test_split
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
# Fetch api
yf.pdr_override()

#Algorithm
stock = input("Enter the stock symbol : ") #Asks for stock ticker
prices = pdr.get_data_yahoo(stock, start, now)
smasUsed=[10,30,50] #Choose smas
start =dt.datetime(2020,1,1)- dt.timedelta(days=max(smasUsed)) #Sets start point of dataframe
now = dt.datetime.now() #Sets end point of dataframe
print(prices)
#Frontend Data pipeline
