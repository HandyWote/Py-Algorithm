class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def dfs(n: int, s: int):
            nonlocal ans
            if n+s < numExchange:
                return
            temp = (n+s)//numExchange
            s = (n+s)%numExchange
            ans += temp
            dfs(temp, s)
            return
        ans = numBottles
        dfs(numBottles, 0)
        return ans

if __name__ == "__main__":
    obj = Solution()
    print(obj.numWaterBottles(15,4))