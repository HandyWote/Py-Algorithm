from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d = defaultdict(list)
        for row, seat in reservedSeats:
            d[row].append(seat)
        
        # 总答案初始为所有行都放 2 个家庭
        ans = 2 * n
        
        # 只处理有预订的行，减去该行达不到 2 的差额
        for row in d:
            cnt = self.count(d[row])   # 该行实际可安排的家庭数（0~2）
            ans -= (2 - cnt)           # 扣除默认 2 与实际数的差值
        
        return ans

    def count(self, reservedRow: List[int]) -> int:
        cnt = 0
        seats = [True] * 10
        for i in reservedRow:
            seats[i-1] = False
        if all(seats[1:5]):   # 左块 2-5
            for i in range(1, 5):
                seats[i] = False
            cnt += 1
        if all(seats[3:7]):   # 中块 4-7
            for i in range(3, 7):
                seats[i] = False
            cnt += 1
        if all(seats[5:9]):   # 右块 6-9
            for i in range(5, 9):
                seats[i] = False
            cnt += 1
        return cnt