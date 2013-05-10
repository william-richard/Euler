'''
Created on Jan 31, 2013

@author: Will
'''
from util.factor import factor, factorNoN



def isAmicable(a):
    aFactors = factorNoN(a)
    aFactSum = sum(aFactors)
    if a == aFactSum:
        return False
    bFactors = factorNoN(aFactSum)
    bFactSum = sum(bFactors)
    return a == bFactSum

if __name__ == '__main__': 
    allAmicables = list()
    for i in range(10000):
        if isAmicable(i):
            allAmicables.append(i)
           
    print allAmicables
    print sum(allAmicables) 