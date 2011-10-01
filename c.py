'''
Created on 2011/10/01

@author: mutouyutaka
'''


import sys


def main() :
    lineNum   = sys.stdin.readline()
    lineNum   = int(lineNum)
    
    for i in range(0, lineNum) :
        N = sys.stdin.readline()
        N = int(N)
        
        max = getN(N)
        t1  = format(max, 'b')
        t2  = format(N - max, 'b')
        st1 = len(t1.split("1")) - 1 if t1.find('1') > -1 else 0
        st2 = len(t2.split("1")) - 1 if t2.find('1') > -1 else 0
        
        print "Case #" + str(i + 1) + ": " + str(st1 + st2)

def getN(n) :
    b = 1
    if n <= 2 :
        return 1
    while n > b :
        b = b * 2
        if n == b - 1 :
            return b - 1
    return (b / 2) - 1

main()