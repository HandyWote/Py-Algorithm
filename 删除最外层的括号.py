
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        primitive_stings: list[str] = self.primitive(s)
        res: str = ''
        for string in primitive_stings:
            res += self.remove(string)
        return res

    @staticmethod
    def primitive(s: str) -> list[str]:
        res: list[str] = []
        left_rem = 0
        n_string = ''
        for i in s:
            n_string += i
            if i == '(':
                left_rem += 1
            elif i == ')':
                left_rem -= 1
                if left_rem == 0:
                    res.append(n_string)
                    n_string = ''
        return res
    
    @staticmethod
    def remove(s: str) -> str:
        res = s[1:len(s)-1]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.removeOuterParentheses("(()())(())(()(()))"))
