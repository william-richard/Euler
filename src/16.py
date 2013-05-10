'''
Created on Oct 19, 2012

@author: wrichard
'''

if __name__ == '__main__':
    exp = 1000
    pro = 2 ** exp
    digits = [int(x) for x in str(pro)]
    print digits
    print sum(digits)