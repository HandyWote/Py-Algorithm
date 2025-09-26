class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = [[1]]
        for i in range(1, n):
            temp = []
            c = 1
            for j in range(1, len(res[-1])):
                if res[-1][j] == res[-1][j - 1]:
                    c += 1
                else:
                    temp.append(c)
                    temp.append(res[-1][j - 1])
                    c = 1
            res.append(temp + [c, res[-1][-1]])
        return ''.join(map(str, res[-1]))
        

if __name__ == "__main__":
    obj = Solution()
    print(obj.countAndSay(4))