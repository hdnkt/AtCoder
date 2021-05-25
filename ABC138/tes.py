from collections import deque 
#スタック
s = deque([])
s.append((1,2))  # [1] for の中でappendするときは s_App = s.appendとか先にやっておく
s.append([2,3])  # [1, 2]
s.append([3,4])  # [1, 2, 3]
a,b = s.pop()
print(a,b)
print(s.pop())
print(s.pop())