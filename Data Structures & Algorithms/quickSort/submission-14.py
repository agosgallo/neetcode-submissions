# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def divide(pairs, start, end):
    pivot = pairs[end].key
    i = start
    for j in range(start, end):
        if pairs[j].key < pivot:
            pairs[i], pairs[j] = pairs[j], pairs[i]
            i += 1
    pairs[i], pairs[end] = pairs[end], pairs[i]
    return i

def quick(pairs, left, right):
    if left < right:
        pivot = divide(pairs, left, right)
        quick(pairs, left, pivot - 1)
        quick(pairs, pivot + 1, right)


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        left = 0
        right = len(pairs) - 1
        quick(pairs, left, right)
        return pairs
            
            
