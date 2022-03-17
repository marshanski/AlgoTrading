__author__ = 'Raz Marshanski'
'''--------------------------------------------------------------------------------------------
Description: This class is having a ROE Valuation procedure
-----------------------------------------------------------------------------------------------'''
'''-----------------------------------------imports--------------------------------------------'''
import yfinance as yf
'''-----------------------------------------constants------------------------------------------'''
ExpectedGrowthRate     = 0.0986
MarginOfSafety         = 0.75
ConservativeGrowthRate = (ExpectedGrowthRate * MarginOfSafety)
DiscountRate           = 0.09
'''--------------------------------------------------------------------------------------------'''
def calculateRoeValuation(ticker):
    '''
    :param ticker: s stock symbol
    :return: the interstic value of a stock, calcuating by ROE model of valuaation
    '''
    '''yahoo finance variables'''
    stock                  = yf.Ticker(ticker)
    sharesOutstanding      = stock.info['sharesOutstanding']
    ROE                    = stock.info['returnOnEquity']
    dividendRate           = checkingDividend(stock.info['dividendRate'])


    totalStockholderEquity = stock.balancesheet.loc['Total Stockholder Equity'].fillna(0)
    shareHoldersEquity     = totalStockholderEquity[0]/sharesOutstanding
    netIncomes             = stock.financials.loc['Net Income'].fillna(0)
    years                  = len(stock.financials.columns)
    aveageRoe              = 0

    for netIncome,equity in zip(netIncomes,totalStockholderEquity):
        aveageRoe += (netIncome/equity)/ years

    sumNpvDividends    = 0
    for i in range(10):
        dividendRate       = dividendRate       * (1+ConservativeGrowthRate)
        shareHoldersEquity = shareHoldersEquity * (1+ConservativeGrowthRate)
        sumNpvDividends   += dividendRate/pow(1+DiscountRate,i)

    return (shareHoldersEquity * aveageRoe / DiscountRate)/pow(1+DiscountRate,10) + sumNpvDividends



def checkingDividend(dividendRate):
    if isinstance(dividendRate, float ):
        return dividendRate
    else:
        return 0







