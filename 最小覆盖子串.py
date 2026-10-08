
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        # 第一步：统计 t 中每个字符需要多少个
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        
        # 第二步：滑动窗口法
        left = 0
        min_len = float('inf')
        result = ""
        window_count = defaultdict(int)
        matched = 0
        
        # 第三步：从左到右扩展窗口
        for right, char in enumerate(s):
            if char in need:
                window_count[char] += 1
                if window_count[char] == need[char]:
                    matched += 1
            
            # 第四步：当所有字符都匹配时，尝试缩小窗口
            while matched == len(need) and left <= right:
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    result = s[left:right+1]
                
                left_char = s[left]
                if left_char in need:
                    window_count[left_char] -= 1
                    if window_count[left_char] < need[left_char]:
                        matched -= 1
                left += 1
        
        return result

def test():
    cases = {
        'input':[
            ("ADOBECODEBANC", 'ABC'),
            ('a', 'a'),
            ('a', 'aa')
        ],
        'output': [
            'BANC',
            'a',
            ''
        ]
    }
    s = Solution()
    for i, c in enumerate(cases['input']):
        assert s.minWindow(c[0], c[1]) == cases['output'][i], f"Test {i+1} faild, expected {cases['output'][i]} but get {s.minWindow(c[0], c[1])}"
        print(f"Test {i+1} passed")
    print('All test passed')

if __name__ == '__main__':
    test()