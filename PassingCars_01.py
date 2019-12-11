# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 50 %
# 시간복잡도 O(N ** 2)

def solution(A):
    # write your code in Python 3.6
    res = 0
    N = len(A)
    
    for i in range(0, N):
        if(res>1000000000):
            return -1
        if(A[i]==1):
            continue
        for j in range(i+1, N):
            if(A[i]!=A[j]):
                res += 1
    
    return res
