from collections import deque

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        q: deque[int] = deque([0])
        for i in s:
            match i:
                case ')':
                    v: int = q.pop()
                    score: int = 1 if v == 0 else 2*v
                    q[-1] += score
                case '(':
                    q.append(0)
        return q[0]

if __name__ == "__main__":
    s = Solution()
    print(s.scoreOfParentheses("(()(()))"))
