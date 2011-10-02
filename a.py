'''
Created on 2011/10/01

'''


import sys


def main() :
    lineNum   = sys.stdin.readline()
    lineNum   = int(lineNum)
    
    for i in range(0, lineNum) :
        firstline = sys.stdin.readline()
        baseData  = firstline.split(" ")
        cardNum   = int(baseData[0])
        cutNum    = int(baseData[1])
        position  = int(baseData[2])
        
        answer    = position
        moveNum   = 0
        list      = {}
        list[1]   = [1, cardNum]
        
        for j in range(0, cutNum) :
            data = sys.stdin.readline()
            data = data.split(" ")
            A    = int(data[0])
            B    = int(data[1])
            
            isAdd = False
            tmp   = {}
            keys  = list.keys()
            keys.sort()
            for k in keys :
                m = list.get(k)
                if A <= k + m[1] - 1 and k <= A + B - 1 :
                    if A <= k and k + m[1] <= A + B :
                        num = k - A + 1
                        tmp[num] = m
                        
                        if A == k :
                            isAdd = True
                    elif A > k and A + B < k + m[1] :
                        delta = (A + B - 1) - k
                        tmp[1]     = [m[0] + (A - k), B]
                        tmp[B + k] = [m[0], A - k]
                        tmp[A + B] = [m[0] + B + (A- k), k + m[1] - (A + B)]
                        isAdd = True
                    elif A > k :
                        num = k + m[1] - A
                        tmp.setdefault(B + k, [m[0], m[1] - num])
                        
                        tmp.setdefault(1, [m[0] + (m[1] - num), num])
                        isAdd = True
                    else :
                        num = A + B - k
                        tmp.setdefault(k + num, [m[0] + num, m[1] - num])
                        
                        tmp.setdefault(B - num + 1, [m[0], num])
                else :
                    if A > k :
                        tmp.setdefault(k + B, m)
                    else :
                        tmp.setdefault(k, m)
            if isAdd == False :
                tmp.setdefault(1, [A, B])
            list = tmp
        
        ks = list.keys()
        ks.sort()
        
        for k in ks :
            if k + list.get(k)[1] > position:
                answer = list.get(k)[0] + (position - k)
                print "Case #" + str(i + 1) + ": " + str(answer)
                break


main()