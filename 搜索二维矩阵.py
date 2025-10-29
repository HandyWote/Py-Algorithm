class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        u, b = 0, len(matrix)-1
        r0 = len(matrix[0])-1
        while u <= b:
            m = (u+b)//2
            if matrix[m][-1] >= target >= matrix[m][0]:
                l, r = 0, r0
                while l <= r:
                    m1 = (l+r)//2
                    if matrix[m][m1] == target:
                        return True
                    elif matrix[m][m1] < target:
                        l = m1 + 1
                    else:
                        r = m1 - 1
                return False
            elif matrix[m][-1] < target:
                u = m + 1
            elif matrix[m][0] > target:
                b = m - 1
        return False


def test():
    s = Solution()
    cases = {
        'input': [
            ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
            ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
            ([[1]], 2)
        ],
        'output':[
            True,
            False,
            False
        ]
    }
    for i, c in enumerate(cases['input']):
        assert s.searchMatrix(c[0], c[1]) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.searchMatrix(c[0], c[1])}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == '__main__':
    test()