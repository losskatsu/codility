# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 66%
# O(N**2)

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    half = N/2
    
    ## solve by using dictionary
    dic = {}
    for ele in A:
        dic[ele] = []
    
    for i in range(0, N):
        for key in dic.keys():
            if(A[i]==key):
                dic[key].append(i)
                if(len(dic[key])>half):
                    return i
    
    return -1
    
