__author__ = 'Raz Marshanski'
'''--------------------------------------------------------------------------------------------
Description: This class is present the eigen values and the photos before and after the reductiom.
-----------------------------------------------------------------------------------------------'''
'''-----------------------------------------imports--------------------------------------------'''
from additiveFunc  import  *
'''-----------------------------------------constants------------------------------------------'''
VALUATION_LST = [peValuationCheck, dcfValuationCheck , roeValuationCheck]
'''--------------------------------------------------------------------------------------------'''
if __name__ == '__main__':
    ticker = input("Please enter a ticker : ")
    value  = 0
    mone   = 0

    for checkingValueProcedure in VALUATION_LST:
        valuation,exsist = checkingValueProcedure(ticker)
        value += valuation
        mone  += exsist

    if(mone>0):
        print("The calculated value of the stock : " + str(value/mone))
    else:
        print("There is no calculated value for this stock")



