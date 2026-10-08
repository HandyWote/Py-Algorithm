import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def init(max_n):
    c0 = [0] * (max_n + 1)
    c1 = [0] * (max_n + 1)
    inv = [0] * (max_n + 1)
    c0[1], c1[1] = 1, 0  # S1 = "0"
    c0[2], c1[2] = 0, 1  # S2 = "1"
    for i in range(3, max_n + 1):
        c0[i] = (c0[i - 2] + c0[i - 1]) % MOD
        c1[i] = (c1[i - 2] + c1[i - 1]) % MOD
        inv[i] = (inv[i - 2] + inv[i - 1] + c1[i - 2] * c0[i - 1]) % MOD
    return inv

def main():
    t = int(input())
    ns = [int(input()) for _ in range(t)]
    inv = init(max(ns))
    print('\n'.join(str(inv[n]) for n in ns))

if __name__ == "__main__":
    main()

