class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = list()
        for x in range(n+1):
            dp.append(0)
        dp[1] = 1
        dp[2] = 2
        
        # since the person can either step 1 or 2, dp[i] is equal to the number of steps from i-1 plus the number of steps from i-2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        # last element represents the number of ways
        return dp[-1]
