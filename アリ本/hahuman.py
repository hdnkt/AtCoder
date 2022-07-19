N = int(input())
L = list(map(int,input().split()))
L.sort(reverse=True)
print(L)
cost=0
while(len(L)-1):
    L.sort(reverse=True)#最小二つを得るだけならソートするのは計算量の無駄だわね
    L[len(L)-2]= L[len(L)-1] + L[len(L)-2]
    L.pop()
    cost+= L[len(L)-1]
    print(cost)
print(cost)