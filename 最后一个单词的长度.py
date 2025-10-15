class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0

    def test(self):
        assert self.lengthOfLastWord("Hello World") == 5, str(self.lengthOfLastWord("Hello World"))
        assert self.lengthOfLastWord("   fly me   to   the moon  ") == 4, str(self.lengthOfLastWord("   fly me   to   the moon  "))
        assert self.lengthOfLastWord("luffy is still joyboy") == 6, str(self.lengthOfLastWord("luffy is still joyboy"))
        print("All tests passed.")

if __name__ == "__main__":
    s = Solution()
    s.test()