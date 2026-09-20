class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = (len(matrix)-1)
        l = 0
        r = len(matrix[0])-1
        MID = 0
        while L <= R:
            MID = (L+R) // 2
            if matrix[MID][0] > target:
                R = MID - 1
            elif matrix[MID][r] < target:
                L = MID + 1
            else:
                break
        while l <= r:
            mid = (l+r) // 2
            if matrix[MID][mid] > target:
                r = mid - 1
            elif matrix[MID][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        


