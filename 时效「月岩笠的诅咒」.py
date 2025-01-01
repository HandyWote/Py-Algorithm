a = input().split()
parts_a = a[0].split('.')
parts_b = a[1].split('.')
if parts_a[1] == parts_b[1]:
    print("YES")
else:
    print("NO")