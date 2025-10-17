from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == len(s):
                return 0
            
            def get_res(new_bit: int, next_can_change: bool) -> int:
                next_mask = mask | new_bit
                # 如果不同字符数量超过k，需要新分区
                if bin(next_mask).count('1') > k:
                    return 1 + dp(i + 1, next_can_change, new_bit)
                # 否则继续当前分区
                return dp(i + 1, next_can_change, next_mask)
            
            # 不改变当前字符的情况
            res = get_res(1 << (ord(s[i]) - ord('a')), can_change)
            
            # 如果可以改变字符，尝试改变为所有可能的字符
            if can_change:
                for j in range(26):
                    res = max(res, get_res(1 << j, False))
            
            return res
        
        return dp(0, True, 0) + 1

def test():
    test_cases = [
        {
            "input": {"s": "accca", "k": 2},
            "expected": 3,
            "description": "基本测试用例1"
        },
        {
            "input": {"s": "aabaab", "k": 3},
            "expected": 1,
            "description": "基本测试用例2"
        },
        {
            "input": {"s": "xxyz", "k": 1},
            "expected": 4,
            "description": "基本测试用例3"
        },
        {
            "input": {"s": "aca", "k": 2},
            "expected": 2,
            "description": "基本测试用例4"
        }
    ]
    solution = Solution()
    for case in test_cases:
        result = solution.maxPartitionsAfterOperations(**case["input"])
        assert result == case["expected"], f"Test failed for {case['description']}: expected {case['expected']}, got {result}"
    print("All tests passed.")

if __name__ == "__main__":
    test()
    # s = "accca"
    # k = 2
    # print(Solution().maxPartitionsAfterOperations(s, k))