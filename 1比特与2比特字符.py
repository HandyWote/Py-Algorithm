class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        if bits[-1] == 0:
            i = 0
            while i < len(bits) - 1:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
            if i == len(bits) - 1:
                return True
        return False

if __name__ == "__main__":
    cases = {
        'input': [[1, 0, 0], [1, 1, 1, 0]],
        'output': [True, False]
    }
    from test import test
    t = test(cases, Solution(), 'isOneBitCharacter')
    t.run()