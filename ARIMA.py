
import pandas as pd
import numpy as np
from pandas import datetime
from statsmodels.tsa.arima_model import ARIMA, AR
from sklearn.metrics import mean_squared_error
import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0


warnings.simplefilter('ignore', ConvergenceWarning)


class main():

    def __init__(self):
        self.df = pd.read_csv(r'D:\Finance project\engine files\orcl-1995-2014.txt') #replace with s&p 500 data then day trade that data from the paper#
        self.test_ar = np.zeros(np.shape(self.df)) # ar_w in literature
        self.predictions = np.zeros(np.shape(self.df))
        self.ar_cash = np.zeros(np.shape(self.df))
        self.time_window = 30
        self.ar_cash[0] = 1000
    def run(self):
        for i , x in enumerate(self.df['Close'][:-1], 0):
            self.predictions[i] = x #?
            if i >= self.time_window:
                self.X = self.df['Close'][0:i]
                self.train = self.X
                self.model = ARIMA(self.train, order=(5,1,0))
                self.model_fit = self.model.fit(disp=0)
                self.output = self.model_fit.forecast()
                self.predictions[i] = self.output[0] #?
                if self.output[0] > x:
                    self.test_ar[i+1] = self.test_ar[i]
                    self.ar_cash[i+1] = self.ar_cash[i]
                if self.output[0] < x:
                    self.ar_cash[i+1] = self.test_ar[i]*x + self.ar_cash[i]
                    self.test_ar[i+1] = 0
                if self.output[0] == x:
                    self.test_ar[i+1] = self.test_ar[i]
                    self.ar_cash[i+1] = self.ar_cash[i]

    def testing(self):
        self.predictions[i+1] = self.df[len(self.df)-1]
        self.ar_strategy = [a*b for a,b in zip(self.test_ar,self.df)] + ar_cash
        self.totret_ar = (self.ar_strategy[-1] - self.ar_strategy[0]) / self.ar_strategy[0]
        #log returns cumulative and relative
        ret_ar_strategy = np.log(self.ar_strategy[1:]/self.ar_strategy[:-1])
        cum_ret_ar_strategy = cum_ret_ar_strategy.cumsum()
        cum_ret_ar_strategy_relative = np.exp(cum_ret_ar_strategy) - 1

ls = main()
ls.run()



# todo:
# analyze program to replicate a better version of it
# work on frontend crypto and stock charts both interative chart
# notifications
# newsfeed for spesific tickers
#backtrade: scrap the backtrade module (doesnt seem to be working) use the paper
#backtrading strategy
#ps: next strategy code backtrading while coding the strategy and trade terms
