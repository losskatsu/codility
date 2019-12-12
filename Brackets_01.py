# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 37%
# 인터넷에서 다른 사람이 푼거보고쓴거라 내 실력이 아님

def solution(S):
    # write your code in Python 3.6
    stackS = []
    
    for symb in S:
        if( (symb=="{") | (symb=="[") | (symb=="(") ):
            stackS.append(symb)
        else:
            tmpSymb = stackS.pop()
            if(tmpSymb=="{"):
                if(symb!="}"):
                    return 0
            if(tmpSymb=="["):
                if(symb!="]"):
                    return 0
            if(tmpSymb=="("):
                if(symb!=")"):
                    return 0
                    
    if(len(stackS)>0):
        return 0
        
    return 1
    
