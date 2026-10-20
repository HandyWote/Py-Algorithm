
from collections.abc import Iterator
from math import isqrt


def divisors(n: int) -> Iterator[int]:
    """按从小到大产出 n 的所有正因数。"""
    i: int
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


class SortableIntegersSolver:
    """
    判断数组 nums 在哪些块大小 k 下"按 k 分块、块内旋转后整体非递减"成立，
    并返回所有满足条件的块大小之和。
    """

    # 实例属性类型声明（只声明，不赋值）
    _nums: list[int]
    _n: int
    _next_descent_at: list[int]

    def __init__(self, nums: list[int]) -> None:
        self._nums = nums
        self._n = len(nums)
        self._next_descent_at = self._build_next_descent_table()

    # ------------------------------------------------------------------
    # 预处理
    # ------------------------------------------------------------------
    def _build_next_descent_table(self) -> list[int]:
        n: int = self._n
        table: list[int] = [n] * n
        nearest_descent: int = n
        i: int
        for i in range(n - 2, -1, -1):
            if self._nums[i] > self._nums[i + 1]:
                nearest_descent = i
            table[i] = nearest_descent
        return table

    # ------------------------------------------------------------------
    # 单块判定
    # ------------------------------------------------------------------
    def _block_max_if_valid(
        self,
        left: int,
        right: int,
        lower_bound: int,
    ) -> int | None:
        """
        检查闭区间 [left, right] 作为一块是否合法。

        合法时返回"该块旋转后有序序列的最大值"，否则返回 None。
        lower_bound 为前一块旋转后的最大值，当前块最小值不得小于它。
        """
        nums: list[int] = self._nums
        pivot: int = self._next_descent_at[left]

        if pivot >= right:
            # 情形一：块内已经非递减，无需旋转。
            if nums[left] < lower_bound:
                return None
            return nums[right]

        # 情形二：块内恰好有一个下降点 pivot，把块分成前后两段。
        # 旋转后，后段整体拼接在前段之前。
        second_start: int = pivot + 1
        if self._next_descent_at[second_start] < right:
            return None  # 后段内部还有下降点，一次旋转无法排好序
        if nums[second_start] < lower_bound:
            return None  # 后段最小值低于上一块最大值
        if nums[right] > nums[left]:
            return None  # 后段最大值超过前段最小值
        return nums[pivot]

    # ------------------------------------------------------------------
    # 块大小判定
    # ------------------------------------------------------------------
    def is_valid_block_size(self, block_size: int) -> bool:
        """判断按 block_size 分块时，每一块都满足条件。"""
        previous_max: int = 0
        right: int
        for right in range(block_size - 1, self._n, block_size):
            left: int = right - block_size + 1
            block_max: int | None = self._block_max_if_valid(
                left, right, previous_max
            )
            if block_max is None:
                return False
            previous_max = block_max
        return True

    # ------------------------------------------------------------------
    # 对外主入口
    # ------------------------------------------------------------------
    def sum_valid_block_sizes(self) -> int:
        return sum(
            k
            for k in divisors(self._n)
            if self.is_valid_block_size(k)
        )


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        return SortableIntegersSolver(nums).sum_valid_block_sizes()
