n = int(input())
#傻不垃圾数列
limit = 301
s = []
answer = []
a,b = 0,1
for p in range(limit):
    a,b = b,a+b
    s.append(a)
#取数
for i in range (n):
    a = int(input()) - 1
    answer.append(s[a])
#输出出
for o in answer:
    print(o)