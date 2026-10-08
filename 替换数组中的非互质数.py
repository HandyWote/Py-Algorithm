import math
class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        st = []
        for x in nums:
            while st:
                g = math.gcd(x, st[-1])
                if g > 1:
                    x = abs(x * st.pop()) // g
                else:
                    break
            st.append(x)
        return st

if __name__ == "__main__":
    # nums = [2,2,1,1,3,3,3]
    nums = [287,41,49,287,899,23,23,20677,5,825] #[2009,20677,825]
    ob = Solution()
    print(ob.replaceNonCoprimes(nums))