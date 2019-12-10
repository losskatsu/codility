# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 100 %

def solution(A):
    # write your code in Python 3.6
    
    N = len(A)
    sortA = A
    sortA.sort()
    diff = []
    res = 1
    
    if((N==1) & (A[0] != 1)):
        res = 0
        return res
    
    if(sortA[0]!=1):
        res = 0
        return res
    
    for i in range(1, N):
        tmp_diff = sortA[i] - sortA[i-1]
        diff.append(tmp_diff)
    
    uniDiff = list(set(diff))
    
    for ele in uniDiff:
        if(ele != 1):
            res = 0
        
    return res    
