from collections import deque


class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)
        min_q = deque()
        max_q = deque()
        f = [0] * (n + 1)
        f[0] = 1
        sum_f = 0
        left = 0

        for i, x in enumerate(nums):
            # 1. 入
            sum_f += f[i]

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            # 2. 出
            while nums[max_q[0]] - nums[min_q[0]] > k:
                sum_f -= f[left]
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            # 3. 更新答案
            f[i + 1] = sum_f % MOD

        return f[n]

if __name__ == "__main__":
    cases = {
        'input':[
            ([9,4,1,3,7], 4),
            ([3,3,4], 0)
        ],
        'output':[
            6,
            2
        ]
    }
    from test import Test
    Test(cases, Solution(), 'countPartitions').run()