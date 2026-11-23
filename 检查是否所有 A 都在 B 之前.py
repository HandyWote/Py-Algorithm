class Solution:
    def checkString(self, s: str) -> bool:
        flag: bool = False
        for i in s:
            if i == 'b':
                flag = True
            else:
                if flag:
                    return False
        return True

