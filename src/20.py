'''
Created on Oct 19, 2012

@author: wrichard
'''
import math

if __name__ == '__main__':
    base = 100
    fact = math.factorial(base)
    digits = [int(x) for x in str(fact)]
    print sum(digits)