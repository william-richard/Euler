'''
Created on Feb 1, 2013

@author: Will
'''
import itertools

if __name__ == '__main__':
    tot = 0
    exponent = 4
    numDigits = 2
    i = 10 ** (numDigits - 1)
    foundAValue = False
    while True:
        digitPowSum = sum([int(p) ** exponent for p in str(i)])
        if i % 10 ** (numDigits - 1) == 0:
            print i, digitPowSum            
        if i == digitPowSum: 
            tot += i
        if len(str(i)) == len(str(digitPowSum)):
            foundAValue = True
        if len(str(i)) > numDigits:
            break
        if len(str(i)) < len(str(digitPowSum)):
            if not foundAValue:
                break
            else:
                numDigits += 1
                i = 10 ** (numDigits - 1)
                print numDigits
        else:
            i += 1
        
    print tot