'''
Created on Oct 19, 2012

@author: wrichard
'''
from util.triangle import triangleNumber
from util.factor import factor, numFactors
import cProfile

def main():
    divisorTarget = 500
    i = 0
    maxSoFar =0
    while maxSoFar < divisorTarget:
        i += 1
        #factors = factor(triangleNumber(i))
        nFactors = numFactors(triangleNumber(i))
        if i % 1000 == 0:
            print "On triangle number %d = %d - %d factors. Max so far = %d" % (i, triangleNumber(i), nFactors, maxSoFar)
        maxSoFar = max(maxSoFar, nFactors) 
    print triangleNumber(i), 'with', numFactors(triangleNumber(i)), 'divisors'
    
if __name__ == '__main__':
    #cProfile.run('main()')
    main()