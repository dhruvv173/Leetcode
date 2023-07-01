from  heapq import heappop, heappush, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        heapify(maxHeap)
        for point in points:
            x,y = point[0], point[1]
            #calc distance for both the points from origin
            dist = (x ** 2 + y ** 2) #can just store the dist instead of sqrt(dist)
            #append the dist first so the heap is sorted by dist
            heappush(maxHeap, (-dist, point))  # -dist cus using maxHeap

            if len(maxHeap) > k:
                heappop(maxHeap)
        for _, point in maxHeap:
            res.append(point)
        return res