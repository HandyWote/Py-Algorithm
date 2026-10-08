MOD = 10**9 + 7

def fast_pow(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

# 计算各部分的值
pow9 = fast_pow(9, 10000, MOD)
pow8 = fast_pow(8, 10000, MOD)
pow7 = fast_pow(7, 10000, MOD)

# 应用容斥原理
result = (pow9 - 2 * pow8 + pow7) % MOD

# 确保结果为正
if result < 0:
    result += MOD

print(result)