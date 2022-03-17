__author__ = 'Raz Marshanski'
'''--------------------------------------------------------------------------------------------
Description: This class is present the eigen values and the photos before and after the reductiom.
-----------------------------------------------------------------------------------------------'''
'''-----------------------------------------imports--------------------------------------------'''
import pandas
import numpy
import yfinance as yf
from   finvizfinance.quote import finvizfinance
from   yahoo_fin.stock_info import *
import numpy    as np
from   datetime import date
'''-----------------------------------------constants------------------------------------------'''

'''--------------------------------------------------------------------------------------------'''
def calculatePeValuation(stock):
    '''finviz variables'''
    stockFinviz  = finvizfinance(stock)
    fundament    = stockFinviz.ticker_fundament()
    EPS          = float(fundament['EPS (ttm)'])
    growthRate   = float(fundament['EPS next 5Y'][0:-1])
    '''yahoo finance variables'''
    stock        = yf.Ticker(stock)
    incomeStat   = stock.get_financials()
    netIncomes   = incomeStat.loc['Net Income']
    sharesNumber = stock.get_shares()
    medienPE     = 0

    try:
        if sharesNumber.empty == False:
            for netIncome, outStandingShares,year in zip(netIncomes, sharesNumber['BasicShares'], incomeStat):
                lastPrice = stock.history(period='1y', start=datetime.date(year.year, 12, 31), end=datetime.date(year.year + 1, 1, 10))['Close'][:][0]
                medienPE += (lastPrice / (netIncome / outStandingShares)) / len(incomeStat.columns)

    except :
        outStandingShares = stock.get_info()['sharesOutstanding']
        for netIncome,year in zip(netIncomes, incomeStat):
            lastPrice = stock.history(period='1y', start=datetime.date(year.year, 12, 31), end=datetime.date(year.year + 1, 1, 10))['Close'][:][0]
            medienPE += (lastPrice / (netIncome / outStandingShares)) / len(incomeStat.columns)

    worth5Years = (pow(((growthRate*0.75/100)+1),5))*EPS*medienPE
    return (worth5Years/(pow(1.09,5)))








