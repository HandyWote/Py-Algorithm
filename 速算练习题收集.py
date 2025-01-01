n = int(input())
list1 = []
list2 = []
k = []
for i in range(n):
    s = input().split()
    if s[0] == 'a' or 'b' or 'c':
        if s[0] == 'a':
            se = s[1]+'+'+s[2]+'='+str(int(s[1])+int(s[2]))
            list1.append(se)
            list2.append(len(se))
            k.append('+')
        if s[0] == 'b':
            se = s[1]+'-'+s[2]+'='+str(int(s[1])-int(s[2]))
            list1.append(se)
            list2.append(len(se))
            k.append('-')
        if s[0] == 'c':
            se = s[1]+'*'+s[2]+'='+str(int(s[1])*int(s[2]))
            list1.append(se)
            list2.append(len(se))
            k.append('*')

    if s[0] != 'a' and s[0] != 'b' and s[0] != 'c':
        if k[-1] == '+':
            se = s[0]+'+'+s[1]+'='+str(int(s[0])+int(s[1]))
            list1.append(se)
            list2.append(len(se))
        if k[-1] == '-':
            se = s[0]+'-'+s[1]+'='+str(int(s[0])-int(s[1]))
            list1.append(se)
            list2.append(len(se))
        if k[-1] == '*':
            se = s[0]+'*'+s[1]+'='+str(int(s[0])*int(s[1]))
            list1.append(se)
            list2.append(len(se))

for i in range(n):
    print(list1[i])
    print(list2[i])