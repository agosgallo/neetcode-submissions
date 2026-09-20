from functools import lru_cache
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n
        ways = self.climbStairs(n-1)

        return ways + self.climbStairs(n-2)

        