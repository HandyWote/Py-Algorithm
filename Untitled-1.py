def input_array():
    s = input().split()
    return s

def print_array(a):
    print(' '.join(a))

def ps(a):
    t = 0
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
    return a

def ds(a,t):
    l = 0
    h = len(a)-1
    while l <= h:
        m = (l+h)//2
        if a[m] == t:
            return m
        elif a[m] > t:
            h = m - 1
        else:
            l = m + 1
    return -1

def primefactor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(str(i))
    if n > 1:
        factors.append(str(n))
    return '*'.join(factors)

def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1