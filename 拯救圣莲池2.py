import heapq


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve_heap(a, k))
    # print(solve_staircase(a, k))


def solve_heap(a, k):
    """方法一：最大堆，O(k log n)"""
    heap = [-x for x in a]
    heapq.heapify(heap)
    ans = 0
    for _ in range(k):
        if not heap:
            break
        val = -heapq.heappop(heap)
        ans += val
        if val > 1:
            heapq.heappush(heap, -(val - 1))
    return ans


def solve_staircase(a, k):
    """方法三：阶梯数学，O(n log n)"""
    a = sorted(a, reverse=True)
    a.append(0)
    ans = 0
    for i in range(len(a) - 1):
        m = i + 1
        delta = a[i] - a[i + 1]
        need = m * delta
        if need <= k:
            ans += m * (a[i] + a[i + 1] + 1) * delta // 2
            k -= need
        else:
            d = k // m
            rem = k % m
            ans += m * (2 * a[i] - d + 1) * d // 2
            ans += rem * (a[i] - d)
            break
    return ans


if __name__ == '__main__':
    main()
