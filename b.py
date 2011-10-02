'''
Created on 2011/10/01

'''


import sys


def main() :
    lineNum   = sys.stdin.readline()
    lineNum   = int(lineNum)
    
    for i in range(0, lineNum) :
        line = sys.stdin.readline()
        data = line.split(" ")
        N    = int(data[0])
        K    = int(data[1])
        
        G_MAX   = 0
        coffees = []
        curMax  = 0
        maxCoff = {}
        
        for j in range(0, N) :
            line2 = sys.stdin.readline()
            data2 = line2.split(" ")
            dict  = { 'c':int(data2[0]), 't':int(data2[1]), 's':int(data2[2]) }
            coffees.append(dict)
            if dict['s'] > curMax :
                maxCoff = dict
                curMax  = dict['s']
    
        coffees.remove(maxCoff)
        G_MAX = drunk(0, K, maxCoff, coffees, 0)
        
        print "Case #" + str(i + 1) + ": " + str(G_MAX)

def drunk(d, k, cof, coffees, total) :
    
    if cof['t'] < cof['c'] or cof['t'] >= k :
        term  = cof['t'] if k > d + cof['t'] else k - d
        total = total + ((d - term) * cof['s'])
        d = d + cof['t'] if k > d + cof['t'] else k
    else :
        max = 0
        nextMax = {}
        for next in coffees :
            if next['s'] > max and d < next['t'] and next['t'] < cof['t'] : 
                nextMax = next
                max     = next['s']
        if nextMax == {} :
            term  = cof['c'] if k > d + cof['c'] else k - d
            total = total + ((d - term) * cof['s'])
            d = d + cof['c'] if k > d + cof['c'] else k
        else :
            coffees.remove(nextMax)
            if nextMax['t'] < nextMax['c'] :
                term  = nextMax['t'] if k > d + nextMax['t'] else cof['c']
                total = total + ((d - term) * nextMax['s'])
                d = d + nextMax['t'] if k > d + nextMax['t'] else k
            else :
                term  = nextMax['c'] if k > d + nextMax['c'] else cof['t'] - cof['c']
                total = total + ((d - term) * nextMax['s'])
                d = d + nextMax['c'] if k > d + nextMax['c'] else k
        
    if k == d :
        return total
    else :
        max  = 0
        maxC = {}
        for next in coffees :
            if next['s'] > max and d < next['t'] : 
                maxC = next
                max  = next['s']
        if maxC == {} :
            return total
        coffees.remove(maxC)
        return drunk(d, k, maxC, coffees, total)
    
main()