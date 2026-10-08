class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
    print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
    print(s.insert([], [5,7]))  # [[5,7]]
    print(s.insert([[1,5]], [2,3]))  # [[1,5]]
    print(s.insert([[1,5]], [2,7]))  # [[1,7]]