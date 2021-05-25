N,H = map(int,input().split())
C,D,A,B,E = map(int,input().split())#かんちがいしてたからこっちを変える。可読性x

INF = 10**15
ans = INF

#食べない日がi日ある場合の最小値をO(1)で求める
for i in range(N+1):
    tmpans = 0
    #食べる日で達成するべき満足度
    goal = E*i-H
    #いったん食べる日を全部安くすませたとして
    manz = B*(N-i)
    tmpans += A*(N-i)
    #何日分グレードアップしなきゃいけないか考える
    goal -= manz
    if goal >= 0:
        need_gradeup =  goal//(D-B)+1
        if need_gradeup > N-i:
            continue
        else:
            tmpans += need_gradeup*(C-A)
    ans=min(ans,tmpans)

print(ans)