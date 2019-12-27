# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 42%

def solution(N):
    # write your code in Python 3.6
    factor = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            res = i*j
            if(res == N):
                factor.append(i)
                continue
            if(res>N):
                continue
    result_set = set(factor)
    result = len(result_set)
    return result
