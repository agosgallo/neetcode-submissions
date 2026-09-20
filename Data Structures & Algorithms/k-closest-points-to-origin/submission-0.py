def dist(p):
    return p[0]**2 + p[1]**2

def divide(points, start, end):
    pivot = dist(points[start])
    i = start
    j = end
    while True:
        while dist(points[i]) < pivot:
            i += 1
        while dist(points[j]) > pivot:
            j -= 1
        if i >= j:
            return j
        points[i], points[j] = points[j], points[i]
        i += 1
        j -= 1

def quicksort(points, left, right):
    if left < right:
        pivot = divide(points, left, right)
        quicksort(points, left, pivot)
        quicksort(points, pivot + 1, right)
    return points

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left = 0
        right = len(points) - 1
        quicksort(points, left, right)
        quicksort(points,left,right)
        return points[:k]

