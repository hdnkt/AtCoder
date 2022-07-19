import numpy as np

#if文
if 1<2:
    print("true")
elif 2<3:
    print("elifTrue")
else:
    print("出力されるはずもなく")

#疑似for(i=0; i<10; i++)
for i in range(0,10,1):
    print(i)
#pythonならではのやつ
for words in ["soba", "udon"]:
    print(words)

#np.array
arr = np.array([1,2,3])
print(arr)
arrAlt = np.array([i for i in range(0,10,1)])
print(arrAlt)
arr_2d = np.array([[i*j for j in range(0,10,1)] for i in range(0,10,1)])
print(arr_2d)

#標準入力
a=int(input())
#map()はリストの各要素に関数を実行する。（帰り値がリストでないことに注意）spritはsepで文字列を分ける
b,c,d = map(int,input().split(sep=" "))
#リストにしたいときはこれ
e = list(map(int,input().split(sep=" ")))

s=input()
#printf
print("{} {}".format(a+b+c+d,s))

#1文字ずつ分割 a[0]="0" a[1]="1" b[2]="0"
a = list("010")

#フィボナッチ数列（都度記憶版）
a = int(input())
mem = [0 for i in range(0,a+1,1)]

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        if mem[n]!=0:
            return mem[n]
        mem[n] = fib(n-1)+fib(n-2)
        return mem[n]

print(fib(a))

from collections import deque 
#スタック
s = deque([])
s.append(1)  # [1] for の中でappendするときは s_App = s.appendとか先にやっておく
s.append(2)  # [1, 2]
s.append(3)  # [1, 2, 3]
s.pop()      # 一番上から取り除く [1, 2, 3] -> [1, 2]
s.pop()      # [1, 2] -> [1]
s.pop()      # [1] -> []
#キュー
q = deque([])
q.append(1)  # [1]
q.append(2)  # [1, 2]
q.append(3)  # [1, 2, 3]
q.popleft()  # 一番下から取り除く [1, 2, 3] -> [2, 3]
q.popleft()  # [2, 3] -> [3]
q.popleft()  # [3] -> []

#深さ優先探索(計算量でかいよ)
a = list(map(int, input().split(sep=" ")))
k = int(input())
n = len(a)

def dfs(i,A_sum):
    if i == n:
        return A_sum == k
    if dfs(i+1,A_sum):
        return True
    if dfs(i+1,A_sum+a[i]):
        return True
    return False

if dfs(0,0):
    print("Yes")
else:
    print("No")

ord("A")
chr(26)
