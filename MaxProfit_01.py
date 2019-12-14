# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 66%
# O(N**2)

def solution(A):
    # write your code in Python 3.6
    res = 0
    
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if(A[j]>A[i]):
                tmp_res = A[j] - A[i]
                res = max(res, tmp_res)
    
    return res
