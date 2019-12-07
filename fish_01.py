# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 25%

def solution(A, B):
    # write your code in Python 3.6
    alive_A = []
    alive_B = []
    
    for i in range(0, len(A)):
        if (i==0):
            alive_A.append(A[i])
            alive_B.append(B[i])
        else:
            tmp_A = alive_A.pop()
            tmp_B = alive_B.pop()
            if( (tmp_B == B[i]) | (tmp_B < B[i]) ):
                alive_A.append(tmp_A)
                alive_A.append(A[i])
                alive_B.append(tmp_B)
                alive_B.append(B[i])
            else:
                tmp_alive = max(tmp_A, A[i])
                tmp_index = A.index(tmp_alive)
                alive_A.append(tmp_alive)
                alive_B.append(tmp_index)
    result = len(alive_A)
    return result
