n = int(input())#一般的なコイン問題はDP問題。これが貪欲法で解けるのは下のが全部上のの約数だから
count=0
tmp=1000-n
for i in [500,100,50,10,5,1]:
    count+=tmp//i
    tmp = tmp%i
print(count)