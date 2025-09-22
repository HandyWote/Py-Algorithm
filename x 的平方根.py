class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while l+1 < r:
            m = (l+r)//2
            if m*m <= x:
                l = m
            else:
                r = m
        return l

if __name__ == "__main__":
    obj = Solution()
    print(obj.mySqrt(4))
    print(obj.mySqrt(8))