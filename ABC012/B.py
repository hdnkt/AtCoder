N = int(input())

h = N//3600
N=N%3600

m = N//60
N = N%60

h = "0"+str(h)
h = h[len(h)-2:len(h)]

m = "0"+str(m)
m = m[len(m)-2:len(m)]

N = "0"+str(N)
N = N[len(N)-2:len(N)]

H = [h,m,N]

print(":".join(H))