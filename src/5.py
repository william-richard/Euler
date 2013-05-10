'''
Created on Oct 18, 2012

@author: Will
'''

def test(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True

if __name__ == '__main__':
    i = 1
    while True:
        r = test(i)
        if r:
            print i
            exit()
        i += 1
    