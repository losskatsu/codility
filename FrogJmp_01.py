# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

## 44 %

def solution(X, Y, D):
    # write your code in Python 3.6
    curX = X
    res = 0
    
    i = 0
    while(True):
        if(curX >= Y):
            res = i
            break
        else:
            curX += D
            i += 1
        
    return res
        
