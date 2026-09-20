#from functools import lru_cache
#class Solution:
#    @lru_cache
#    def climbStairs(self, n: int) -> int:

#        if n<=2:
#            return n
#        ways = self.climbStairs(n-1)

#        return ways + self.climbStairs(n-2)

class Solution:
    def climbStairs(self,n):
        dp = [1,1]
        for i in range(2,n+1):
            dp.append(dp[i-1]+ dp[i-2])
        return dp[n]