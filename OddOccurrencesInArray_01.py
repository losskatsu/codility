# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    uni_A = set(A)
    dic_A = {}
    for i in uni_A:
        dic_A[i] = 0
    
    for i in A:
        for j in uni_A:
            if(i==j):
                dic_A[j] += 1
    result = 0
    for i in dic_A.keys():
        if(dic_A[i]<2):
            result = i
    
    return result
        
        
