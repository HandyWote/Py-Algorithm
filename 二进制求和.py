class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == '__main__':
    cases = {
        'input':[
            ("11", "1"),
            ("1010", "1011")
        ],
        'output':[
            "100",
            "10101"
        ]
    }
    from test import Test
    Test(cases, Solution(), 'addBinary').run()