__author__ = 'Raz Marshanski'
'''--------------------------------------------------------------------------------------------
Description: This class is present the eigen values and the photos before and after the reductiom.
-----------------------------------------------------------------------------------------------'''
'''-----------------------------------------imports--------------------------------------------'''
from PeValuation  import  *
from DcfValuation  import  *
from RoeValuation  import  *
'''-----------------------------------------constants------------------------------------------'''

'''--------------------------------------------------------------------------------------------'''

def peValuationCheck(ticker):
    try:
        peValuation = calculatePeValuation(ticker)
        print(ticker + " PE Valuation : " + str(peValuation))
        return peValuation,1

    except :
        print("There is no PE Valuation to that stock")
        return 0,0

def dcfValuationCheck(ticker):
    try:
        dcfValuation = calculateDcfValuation(ticker)
        print(ticker + " DCF Valuation : " + str(dcfValuation))
        return dcfValuation,1

    except :
        print("There is no DCF Valuation to that stock")
        return 0,0

def roeValuationCheck(ticker):
    try:
        roeValuation = calculateRoeValuation(ticker)
        print(ticker + " ROE Valuation : " + str(roeValuation))
        return roeValuation,1

    except :
        print("There is no ROE Valuation to that stock")
        return 0,0

