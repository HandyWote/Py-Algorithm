class Solution:
    def simplifyPath(self, path: str) -> str:
        path = list(path.split('/'))
        s_path = []
        for p in path:
            if not p or p == '.': continue
            if p == '..' and s_path:
                s_path.pop() 
                continue
            elif p == '..': continue
            s_path.append(p)
        return '/' + '/'.join(s_path)

def test():
    s = Solution()
    cases = {
        'input': [
            "/home/",
            "/home//foo/",
            "/home/user/Documents/../Pictures",
            "/../",
            "/.../a/../b/c/../d/./"
        ],
        'output': [
            "/home",
            "/home/foo",
            "/home/user/Pictures",
            "/",
            "/.../b/d"
        ]
    }
    for i, input in enumerate(cases['input']):
        output = cases['output'][i]
        assert s.simplifyPath(input) == output, f"Test case {i+1} faild, expected {output} ,but get {s.simplifyPath(input)}"
        print(f"Test case {i+1} passed")

if __name__ == "__main__":
    test()
    # a = list("/home//foo/".split('/'))
    # print(a)