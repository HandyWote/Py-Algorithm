n = int(input())
al = list(map(int, input().split()))
ans = []
current_sum = 0
current_level_count = 0
level = 0  # 当前层数，初始为0，因为后面第一次会变成1层

for num in al:
    current_sum += num
    current_level_count += 1
    if current_level_count == 2 ** level:
        ans.append(current_sum)
        current_sum = 0
        current_level_count = 0
        level += 1

# 处理最后一层可能未满的情况
if current_sum != 0:
    ans.append(current_sum)

# 找到最大值的最小深度
max_sum = max(ans)
for depth, s in enumerate(ans, 1):
    if s == max_sum:
        print(depth)
        break