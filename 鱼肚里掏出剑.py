def get_input():
    n, m = map(int, input().split())
    mitrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mitrix.append([1 if x == 1 else -1 for x in row])
    return n, m, mitrix


def add(tree, x):
    while x < len(tree):
        tree[x] += 1
        x += x & -x


def query(tree, x):
    ans = 0
    while x > 0:
        ans += tree[x]
        x -= x & -x
    return ans


def calc(arr):
    pre = [0]
    s = 0
    for x in arr:
        s += x
        pre.append(s)

    nums = sorted(set(pre))
    mp = {nums[i]: i + 1 for i in range(len(nums))}

    ans = 0
    tree = [0] * (len(nums) + 1)
    for x in pre:
        idx = mp[x]
        ans += query(tree, idx - 1)
        add(tree, idx)
    return ans


def main():
    n, m, mitrix = get_input()
    ans = 0
    for x1 in range(n):
        col = [0] * m
        for x2 in range(x1, n):
            for y in range(m):
                col[y] += mitrix[x2][y]
            ans += calc(col)
    print(ans)


if __name__ == '__main__':
    main()
