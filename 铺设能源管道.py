import sys

n = input()

# def get_cost(i: int):
#     i = str(i)
#     res = sum([int(x) for x in i])
#     return res

# ans = []
# for i in range(n, n*n):
#     ans.append([i, get_cost(i)])

# print(min(ans, key=lambda x: x[1]))

# ==正确答案==
if n == '1':
    print(1)
else:
    i = len(str(int(n)-1))
    print(10 ** i)

# ==错误答案==
# if n == '1':
#     print(1)
#     sys.exit()
# if int(n) % 10 == 0:
#     print(n)
#     sys.exit()
# print ('1'+ len(n) * '0')