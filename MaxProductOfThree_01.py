# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 22%

def solution(A):
    # write your code in Python 3.6
    result = 0
    
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            for k in range(j+1, len(A)):
                multi = A[i]*A[j]*A[k]
                result = max(result, multi)
    
    return result
