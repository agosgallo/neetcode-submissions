# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def merge(pairs,s,m,e):
    insertionpoint = s
    L = pairs[s:m+1]
    R = pairs[m+1:e+1]
    i = 0
    j = 0

    while i < len(L) and j < len(R):
        if L[i].key <= R[j].key:
            pairs[insertionpoint] = L[i]
            i +=1
        else:
            pairs[insertionpoint] = R[j]
            j +=1
        insertionpoint += 1
    while i < len(L):
        pairs[insertionpoint] = L[i]
        i+=1
        insertionpoint += 1
    while j < len(R):
        pairs[insertionpoint] = R[j]
        j += 1
        insertionpoint +=1
def MergeSorting(pairs,s,e):
    if e-s+1<=1:
        return pairs
    m = ((e+s)//2)
    MergeSorting(pairs,s,m)
    MergeSorting(pairs,m+1,e)
    merge(pairs,s,m,e)
    return pairs






class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0
        e = len(pairs)
        MergeSorting(pairs,s,e)

        return pairs
        