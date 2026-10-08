from bisect import bisect_left


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end in intervals:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d = 2 - (st[-1][2] - s)  # 去掉运行中的时间点
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]
    
if __name__ == "__main__":
    from test import Test
    Test(
        cases={
            'input': [[[1,3],[3,7],[8,9]], [[1,3],[1,4],[2,5],[3,5]], [[1,2],[2,3],[2,4],[4,5]]],
            'output': [5, 3, 5],
        },
        solution=Solution(),
        func='intersectionSizeTwo',
    ).run()
