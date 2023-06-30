from  heapq import heappop, heappush, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        heapify(maxHeap)
        for point in points:
            x,y = point[0], point[1]
            dist = (x ** 2 + y ** 2)
            heappush(maxHeap, (-dist, point))

            if len(maxHeap) > k:
                heappop(maxHeap)
        
        for _, point in maxHeap:
            res.append(point)

        return res