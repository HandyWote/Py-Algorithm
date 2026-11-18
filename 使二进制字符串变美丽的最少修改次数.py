class Solution:
    def minChanges(self, s: str) -> int:
        ans: int = 0
        for i in range(0, len(s), 2):
            ans += s[i] != s[i+1]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minChanges("11000111"))
