import sys
from math import sqrt
input = sys.stdin.readline

def get_input() -> list[list[int]]:
    pair: list[tuple[int]] = []
    for _ in range(int(input())):
        pair.append(list(map(int, input().split())))
    return pair

def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if 1 < x <= 3:
        return True
    return all(x % i != 0 for i in range(2, int(sqrt(x)+1)))

def get_prime(x: int) -> set[int]:
    factors = set()
    i = 2
    while i * i <= x:
        if x % i == 0:
            factors.add(i)
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        factors.add(x)
    return factors

def ngcd(pair: list[list[int]]) -> int:
    n: int = len(pair)
    dp: list[set[int]] = [set() for _ in range(n)]
    dp[0] = get_prime(pair[0][0]) | get_prime(pair[0][1])
    for i in range(1, n):
        if not dp[i-1]:
            break
        for j in dp[i-1]:
            # for k in pair[i]:
            #     g: int = math.gcd(j, k)
            #     if g == 1 or not is_prime(g):
            #         continue
            #     dp[i].add(g)
            if pair[i][0] % j == 0 or pair[i][1] % j == 0:
                dp[i].add(j)
    return max(dp[-1]) if dp[-1] else -1




if __name__ == "__main__":
    print(ngcd(get_input()))
    