# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 12%

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    dp = [0]*N
    
    for i in range(0, N):
        if(i==0):
            dp[0] = A[0]
        elif((i>0) & (i<(N-1))):
            dp[i] = max(dp[i-1], dp[i-1] + A[i])
        else:
            dp[i] = dp[i-1] + A[i]
    return dp[N-1]
