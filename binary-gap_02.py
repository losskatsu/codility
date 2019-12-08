# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    ## 10진법 -> 2진법 
    conti = True
    oriN = N
    binN = []
    pos = []
    maxDiff = 0
    
    while(True):
        if(oriN==1):
            binN.append(oriN)
            break
        else:
            newRemain = oriN%2
            oriN = oriN//2
            binN.append(newRemain)

    binN = binN[::-1]
    
    for i in range(0, len(binN)):
        if(binN[i] == 1):
            pos.append(i)

    for i in range(1, len(pos)):
        tmpDiff = pos[i] - pos[i-1] - 1
        maxDiff = max(maxDiff, tmpDiff)
        
    return maxDiff
