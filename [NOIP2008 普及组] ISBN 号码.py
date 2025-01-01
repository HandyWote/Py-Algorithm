s = input()
a = s.replace('-','')

if a[-1] == 'X':
    isbn = 'X'
else:
    isbn = int(a[-1])

j = 0
for i in range(1,10):
    j += int(a[i-1]) * i
j = j % 11

if j == 10:
    j = 'X'

if j == isbn:
    print('Right')
else:
    print(str(a[0])+'-'+str(a[1:4])+'-'+str(a[4:9])+'-'+str(j))