import math
s, v = map(int, input().split())
min_time = math.ceil(s / v + 10)
if min_time <= 480:
    latest_time = 8 * 60 - min_time
    hours = latest_time // 60
    minutes = int(latest_time % 60)
else:
    latest_time = 32 * 60 - min_time
    hours = latest_time // 60
    minutes = int(latest_time % 60)
print(f"{hours:02d}:{minutes:02d}")