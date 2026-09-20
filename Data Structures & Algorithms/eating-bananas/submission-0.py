class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            mid = (start + end)//2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)
            if total_hours <= h:
                end = mid
            else:
                start = mid + 1
        return start