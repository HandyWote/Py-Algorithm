def func():
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    m = float('inf')
    for i in range(k):
        prefix_sum = 0
        cnt = 0
        for j in range(i, n, k):
            prefix_sum += w[j]
            cnt += 1
            avg = prefix_sum // cnt
            m = min(m, avg)
    print(int(m))

if __name__ == "__main__":    func()
