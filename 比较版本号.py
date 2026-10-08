class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = [int(i) for i in version1.split('.')]
        b = [int(i) for i in version2.split('.')]
        a_l = len(a)
        b_l = len(b)
        m_l = min(a_l, b_l)
        for i in range(m_l):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
            else:
                continue
        if a_l == m_l and sum(b[m_l:]) != 0:
            return -1
        elif b_l == m_l and sum(a[m_l:]) != 0:
            return 1
        else:
            return 0

            

if __name__ == "__main__":
    obj = Solution()
    print(obj.compareVersion("1.01", "1.001"))        