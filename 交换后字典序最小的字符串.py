class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)-1):
            x, y = s[i], s[i+1]
            if x > y and (ord(x)+ord(y))%2 == 0:
                s[i+1], s[i] = x, y
                break
        return ''.join(s)
    
if __name__ == "__main__":
    s = "45320"
    obj = Solution()
    print(obj.getSmallestString(s))