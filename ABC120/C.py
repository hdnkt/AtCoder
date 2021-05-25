S = list(map(int,list(input())))
count0 = S.count(1)
count1 = S.count(0)
print(2*min(count0,count1))