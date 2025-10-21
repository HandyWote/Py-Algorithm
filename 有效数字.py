class Solution:
    def isNumber(self, s: str) -> bool:
        if 'e' in s:
            base, exp = s.split('e', 1)
            return self.isDecimal(base) and self.isInteger(exp)
        elif 'E' in s:
            base, exp = s.split('E', 1)
            return self.isDecimal(base) and self.isInteger(exp)
        else:
            return self.isDecimal(s)
    def isDecimal(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ('+', '-'):
            s = s[1:]
        if not s:
            return False
        dot_seen = False
        digit_seen = False
        for char in s:
            if char.isdigit():
                digit_seen = True
            elif char == '.':
                if dot_seen:
                    return False
                dot_seen = True
            else:
                return False
        return digit_seen
    def isInteger(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ('+', '-'):
            s = s[1:]
        if not s:
            return False
        for char in s:
            if not char.isdigit():
                return False
        return True

def test():
    cases = {
        'input': [
            "0",
            "e",
            ".",
            "-.E3"
        ],
        'output': [
            True,
            False,
            False,
            False
        ]
    }
    solution = Solution()
    for i, case in enumerate(zip(cases['input'], cases['output'])):
        input_args, expected = case
        result = solution.isNumber(input_args)
        assert result == expected, f"case {i} failed: expected {expected}, got {result}"
        print(f"case {i} passed")

if __name__ == "__main__":
    test()