import sys

sys.setrecursionlimit(10**6)

N = int(input())
S = list(input())
X = list(input())

dic = {}

def solve(pre):
    if len(pre) in dic:
        if int(pre)%7 in dic[len(pre)]:
            return dic[len(pre)][int(pre)%7]

    if len(pre)==N-1:
        if X[len(pre)]=="T":
            ret= int(pre+"0")%7==0 or int(pre+S[len(pre)])%7==0
        else:
            ret= int(pre+"0")%7==0 and int(pre+S[len(pre)])%7==0
    else:
        if X[len(pre)] == "T":
            ret= solve(pre+"0") or solve(pre+S[len(pre)])
        else:
            ret= solve(pre+"0") and solve(pre+S[len(pre)])

    if len(pre)==0:
        return ret

    if not(len(pre) in dic):
        dic[len(pre)]={}
    dic[len(pre)][int(pre)%7] = ret
    return ret

print("Takahashi" if solve("") else "Aoki")