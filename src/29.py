'''
Created on Feb 2, 2013

@author: Will
'''
import itertools

if __name__ == '__main__':
    aRange = range(2, 101)
    bRange = range(2, 101)
    powComboSet = set()
    for a, b in itertools.product(aRange, bRange):
        powComboSet.add(a ** b)
    print len(powComboSet)