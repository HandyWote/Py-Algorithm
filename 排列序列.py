class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)

    def test(self):
        assert self.getPermutation(3, 3) == "213", str(self.getPermutation(3, 3))
        assert self.getPermutation(4, 9) == "2314", str(self.getPermutation(4, 9))
        assert self.getPermutation(3, 1) == "123", str(self.getPermutation(3, 1))
        print("All tests passed.")

if __name__ == "__main__":
    s = Solution()
    s.test()