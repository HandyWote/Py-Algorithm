class Solution:
    def canAliceWin(self, n: int) -> bool:
        B: set[int] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 20, 21, 22, 23, 24, 25, 26, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 52, 53, 55}
        if n in B:
            return False
        else:
            return True

