n = int(input())
n_list = []
s_list = []
for _ in range(n):
    a = input().split()
    n_list.append(a[0])
    s_list.append(list(map(int,a[1:])))
as_list = [sum(i) for i in s_list]
k = as_list.index(max(as_list))
print(n_list[k],' '.join(map(str,s_list[k])))
