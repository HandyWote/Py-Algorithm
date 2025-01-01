a = input()
ans = 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        ans += 1
    else:
        print(a[i]+str(ans),end='')
        ans = 1
        continue
print(a[-1]+str(ans),end='')