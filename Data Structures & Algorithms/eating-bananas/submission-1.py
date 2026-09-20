import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        sol = r

        while l <= r:
            m = (l+r)//2
            total_hours = 0
            
            for p in piles:
                total_hours += (p+m-1)//m
            
            if total_hours > h:
                l = m+1
            else:
                r = m-1
                sol = min(sol,m)
        return sol