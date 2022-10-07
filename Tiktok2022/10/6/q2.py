class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #纯完全背包，只求凑成总数，无关排列组合。
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])
        
        return dp[-1] if dp[-1] != math.inf else -1
        
        