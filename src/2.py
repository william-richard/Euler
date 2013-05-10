'''
Created on Oct 18, 2012

@author: Will
'''

def fib(a,b,lessThan=0):
    if lessThan > 0 and b >= lessThan:
        return [a]
    p = fib(b, a+b, lessThan)
    p.append(a)
    return p

if __name__ == '__main__':
    print sum([x for x in fib(1,2,4000000) if x % 2 == 0])