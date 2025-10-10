class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        dp = [float('-inf')] * (n+1)
        dp[n-1] = energy[n-1]
        for i in range(n-2, -1, -1):
            if i + k >= n:
                dp[i] = energy[i]
            else:
                dp[i] = dp[i+k] + energy[i]
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.maximumEnergy([5,2,-10,-5,1], 3))  # Expected output: 3
    print(s.maximumEnergy([-2,-3,-1], 2))  # Expected output: -1
    print(s.maximumEnergy([8,-5], 1))  # Expected output: 3