cnt = 0
for b in range(0, 256):
    for r in range(0, 256):
        for g in range(0, 256):
            if b > r and b > g:
                cnt += 1
            else:
                continue
print(cnt)