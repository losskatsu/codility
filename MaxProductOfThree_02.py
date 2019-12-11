# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 44 %

def solution(A):
    # write your code in Python 3.6
    sortA = A
    sortA.sort()
    n = len(A)
    
    pos = sortA[0]*sortA[1]*sortA[2]
    neg = sortA[n-1]*sortA[n-2]*sortA[n-3]
    
    res = max(pos, neg)
    
    return res
    
    
    
