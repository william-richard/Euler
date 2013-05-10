'''
Created on Feb 1, 2013

@author: wrichard
'''

if __name__ == '__main__':
    s = 0
    #for i in range(1,11):
    for i in range(1,1001):
        s += i ** i
    print "%.10i" % (s % 10000000000)