m = int(input())

if m < 100:
    print("00")

if 100<=m and m <= 5000:
    ans = "0"+str(m//100)
    print(ans[len(ans)-2:len(ans)])

if 6000<=m and m<=30000:
    print(m//1000+50)

if 35000<=m and m<=70000:
    print((m//1000-30)//5+80)

if 70000<m:
    print(89)