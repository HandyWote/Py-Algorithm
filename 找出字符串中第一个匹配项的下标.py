class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            s = haystack[i:i+len(needle)]
            if s == needle:
                return i
        return -1
        
if __name__ == "__main__":
    obj = Solution()
    print(obj.strStr("sadbutsad", "sad"))