class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertpoint = m+n-1
        em = m-1
        en = n-1

        while en >= 0:

            if em >= 0 and nums1[em] > nums2[en]:
                nums1[insertpoint] = nums1[em]
                em -= 1
            else:
                nums1[insertpoint] = nums2[en]
                en -= 1
            insertpoint -= 1



