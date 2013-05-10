'''
Created on Oct 19, 2012

@author: Will
'''

def isPythagoreanTriplet(i,j,k):
    #find the max value, i.e. c
    (a,b,c) = sorted([i,j,k])
    return a**2 + b**2 == c**2

if __name__ == '__main__':
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if not a+b+c == 1000:
                    continue
                if isPythagoreanTriplet(a, b, c):
                    print a,b,c
                    print a*b*c
    