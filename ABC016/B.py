A,B,C = map(int,input().split())

an1=0
if A+B==C:
    an1=1
an2=0
if A-B==C:
    an2=1

if an1==1 and an2==1:
    print("?")
elif an1==1:
    print("+")
elif an2==1:
    print("-")
else:
    print("!")


