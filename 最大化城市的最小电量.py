from itertools import accumulate


class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        # 前缀和
        s = list(accumulate(stations, initial=0))
        # 初始电量
        power = [s[min(i + r + 1, n)] - s[max(i - r, 0)] for i in range(n)]

        def check(low: int) -> bool:
            diff = [0] * n  # 差分数组
            sum_d = built = 0
            for i, p in enumerate(power):
                sum_d += diff[i]  # 累加差分值
                m = low - (p + sum_d)
                if m <= 0:
                    continue
                # 需要在 i+r 额外建造 m 个供电站
                built += m
                if built > k:  # 不满足要求
                    return False
                # 把区间 [i, i+2r] 增加 m
                sum_d += m  # 由于 diff[i] 后面不会再访问，我们直接加到 sum_d 中
                if (right := i + r * 2 + 1) < n:
                    diff[right] -= m
            return True

        # 开区间二分
        mn = min(power)
        left, right = mn + k // n, mn + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

def test():
    cases = {
        'input':[
            ([1,2,4,5,0], 1, 2),
            ([4,4,4,4], 0, 3)
        ],
        'output': [
            [3,2,3],
            [1,-1]
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        result = s.maxPower(*c)
        expected = cases['output'][i]
        assert result == expected, f"Test {i+1} failed, expected {expected} but get {result}"
        print(f"Test {i+1} passed")    
    print('All test passed')

if __name__ == "__main__":
    test()