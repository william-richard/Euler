'''
Created on Feb 1, 2013

@author: Will
'''

if __name__ == '__main__':
    print ord('A') - 64
    for i, n in enumerate(sorted(open('./names.txt', 'r').read().split(',') + [''])):
        n = n.strip('"').upper()
        if n == 'COLIN':
            print n
            print i
    print sum([i * sum([ord(c) - 64 for c in s])for i, s in enumerate(sorted([n.strip('"').upper() for n in open('./names.txt', 'r').read().split(',') + ['']]))])
    
    