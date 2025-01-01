n = int(input())
list1 = []
name = []
score = []
#数据搜集
for _ in range(n):
    list1 = input().split()
    name.append(list1[0])
    score.append(list(map(int,list1[1:])))
#处理
for i in range(n):
    for j in range(i+1,n):
        if abs(score[i][0]-score[j][0])<=5 and abs(score[i][1]-score[j][1])<=5 and abs(score[i][2]-score[j][2])<=5 and abs(sum(score[i])-sum(score[j]))<=10:
            print(name[i],name[j])