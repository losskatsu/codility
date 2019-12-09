# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 점수 : 66%
# 시간복잡도 N^2 

def solution(A):
    # write your code in Python 3.6
    uniqA = list(set(A))
    dicA = {}
    
    for i in range(0, len(uniqA)):
        dicA[uniqA[i]] = 0
    
    for ele in A:
        for key in dicA.keys():
            if(ele==key):
                dicA[key] += 1
    
    for key in dicA.keys():
        if(dicA[key]%2 == 1):
            res = key
            break

    return res
    
    
