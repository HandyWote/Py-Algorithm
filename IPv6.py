mod = int(1e9 + 7)
n7 = pow(65536, 7, mod)
n8 = pow(65536, 8, mod)

# 计算 l0
s1 = 1 * 16 + 2 * (255 - 15) + 3 * (4095 - 255) + 4 * (65535 - 4095)
l0 = (s1 * n7 * 8 + 7 * n8) % mod

smax = 0
for i in range(2 ** 8):
    bits = [(i >> k) & 1 for k in range(8)]  # 二进制各位
    # 寻找连续零段的最大收益
    add = 0
    l = 0
    while l < 8:
        if bits[l] == 0:
            r = l
            while r < 8 and bits[r] == 0:
                r += 1
            newadd = 2 * (r - l) - 1 - (l == 0) - (r == 8)   # 边界调整
            add = max(add, newadd)
            l = r
        else:
            l += 1
    smax = (smax + add * pow(65535, sum(bits), mod)) % mod

print((l0 - smax) % mod)