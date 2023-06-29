from heapq import heappop, heappush, heapify
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp = {}
        res = []
        maxHeap = []
        heapify(maxHeap)
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        for num, freq in mp.items():
            heappush(maxHeap, (-freq, num))
        while maxHeap:
            element = heappop(maxHeap)
            freq = element[0]*-1
            for i in range(freq):
                res.append(element[1])
        return res[::-1]