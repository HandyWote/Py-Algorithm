from collections import deque


class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        d = deque()
        d.append(''.join(sorted(words[0])))
        result = [words[0]]
        for word in words[1:]:
            sw = ''.join(sorted(word))
            if not sw in d:
                d.append(sw)
                d.popleft()
                result.append(word)
            continue
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"]))  # ["abba","cd"]
    print(s.removeAnagrams(["a","b","c","d","e"]))  # ["a","b","c","d","e"]
    print(s.removeAnagrams(["a","a","a","b","b","b","a","a"]))  # ["a","b","a"]