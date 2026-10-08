def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_number(num):
    return int(str(num)[::-1])

def find_true_primes(m, n):
    true_primes = []
    for num in range(m, n + 1):
        if is_prime(num) and is_prime(reverse_number(num)):
            true_primes.append(num)
    return true_primes

# 读取输入
m, n = map(int, input().split())

# 找出真素数
result = find_true_primes(m, n)

# 输出结果
if result:
    print(','.join(map(str, result)))
else:
    print("No")