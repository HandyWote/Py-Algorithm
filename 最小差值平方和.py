class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_ops: int = k1 + k2
        pos_diff: list[int] = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(pos_diff) <= total_ops:
            return 0

        pos_diff.sort(reverse=True)
        pos_diff.append(0)
        n: int = len(nums1)

        for i in range(1, n + 1):
            cost: int = (pos_diff[i - 1] - pos_diff[i]) * i
            if cost > total_ops:
                quotient, remainder = divmod(total_ops, i)
                threshold: int = pos_diff[i - 1] - quotient

                high_part: int = pow(threshold, 2) * (i - remainder)
                low_part: int = pow(threshold - 1, 2) * remainder
                tail_part: int = sum(pow(x, 2) for x in pos_diff[i:n])

                return high_part + low_part + tail_part

            total_ops -= cost

        return 0
