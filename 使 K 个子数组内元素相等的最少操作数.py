class LazyHeap:
    def __init__(self):
        self.heap = []
        self.remove_cnt = defaultdict(int)  # 每个元素剩余需要删除的次数
        self.size = 0  # 实际大小
        self.sum = 0  # 堆中元素总和

    # 删除
    def remove(self, x: int) -> None:
        self.remove_cnt[x] += 1  # 懒删除
        self.size -= 1
        self.sum -= x

    # 正式执行删除操作
    def apply_remove(self) -> None:
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heappop(self.heap)

    # 查看堆顶
    def top(self) -> int:
        self.apply_remove()
        return self.heap[0]

    # 出堆
    def pop(self) -> int:
        self.apply_remove()
        self.size -= 1
        self.sum -= self.heap[0]
        return heappop(self.heap)

    # 入堆
    def push(self, x: int) -> None:
        if self.remove_cnt[x] > 0:
            self.remove_cnt[x] -= 1  # 抵消之前的删除
        else:
            heappush(self.heap, x)
        self.size += 1
        self.sum += x

    # push(x) 然后 pop()
    def pushpop(self, x: int) -> int:
        self.apply_remove()
        if not self.heap or x <= self.heap[0]:
            return x
        self.sum += x - self.heap[0]
        return heappushpop(self.heap, x)


class Solution:
    # 480. 滑动窗口中位数（有改动）
    # 返回 nums 的所有长为 k 的子数组的（到子数组中位数的）距离和
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * (len(nums) - k + 1)
        left = LazyHeap()  # 最大堆（元素取反）
        right = LazyHeap()  # 最小堆

        for i, x in enumerate(nums):
            # 1. 进入窗口
            if left.size == right.size:
                left.push(-right.pushpop(x))
            else:
                right.push(-left.pushpop(-x))

            l = i + 1 - k
            if l < 0:  # 窗口大小不足 k
                continue

            # 2. 计算答案
            v = -left.top()
            s1 = v * left.size + left.sum  # sum 取反
            s2 = right.sum - v * right.size
            ans[l] = s1 + s2

            # 3. 离开窗口
            x = nums[l]
            if x <= -left.top():
                left.remove(-x)
                if left.size < right.size:
                    left.push(-right.pop())  # 平衡两个堆的大小
            else:
                right.remove(x)
                if left.size > right.size + 1:
                    right.push(-left.pop())  # 平衡两个堆的大小

        return ans

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        dis = self.medianSlidingWindow(nums, x)
        f = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            f[i][i * x - 1] = inf
            for j in range(i * x, n - (k - i) * x + 1):  # 左右留出足够空间给其他子数组
                f[i][j] = min(f[i][j - 1], f[i - 1][j - x] + dis[j - x])  # j-x 为子数组左端点
        return f[k][n]
