class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

        # return x**n
        
if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.00000, 10))  # Expected output: 1024.00000
    print(s.myPow(2.10000, 3))   # Expected output: 9.26100
    print(s.myPow(2.00000, -2))  # Expected output: 0.25000