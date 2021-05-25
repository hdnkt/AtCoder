a = int(input())
b = int(input())
c = int(input())
x = int(input())
#計算時間縮めるならmaxAとかをXを超えるかの判別で指定（伝われ

counter = 0
for i in range(0,a+1,1):
    for j in range(0,b+1,1):
        for k in range(0,c+1,1):
            if 500*i+100*j+50*k == x:
                counter += 1

print(counter)