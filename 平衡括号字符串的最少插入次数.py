
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0
        for c in s:
            if c == '(':
                need += 2
                if need % 2:
                    ans += 1
                    need -= 1
            else:
                need -= 1
                if need < 0:
                    ans += 1
                    need = 1
        return ans + need

if __name__ == '__main__':
    s = Solution()
    print(s.minInsertions('))())('))
    
    print(s.minInsertions(')())('))

    print(s.minInsertions('))()()))'))
