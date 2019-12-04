# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    currentN = N
    binN = ""
    while(True):
        if(currentN==1):
            binN = binN + "1"
            break
        else:
            tmp_remain = str(currentN%2)
            binN = binN + tmp_remain
            currentN = currentN//2
    binN = binN[::-1]
    bin_one = []
    for i in range(0, len(binN)):
        if(binN[i]=="1"):
            bin_one.append(i)
    
    gap = [0]
    for i in range(0, len(bin_one)-1):
        tmp_gap = bin_one[i+1]-bin_one[i]-1
        gap.append(tmp_gap)
        
    result = max(gap)
    
    return result
