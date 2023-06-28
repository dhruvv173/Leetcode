from heapq import heappop, heappush, heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        minHeap = []
        heapify(minHeap)
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        for num, freq in mp.items():
            heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        while minHeap:
            ans.append(heapq.heappop(minHeap)[1])
        return ans