'''
Created on Oct 18, 2012

@author: Will
'''

def isPalendrome(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    numDigits = 3
    numbers = sorted(range(10**(numDigits-1), 10**(numDigits)),reverse=True)
    m = 0
    for i in numbers:
        for j in numbers:
            p = i*j
            if isPalendrome(p):
                m = max(p, m)
    print m
            