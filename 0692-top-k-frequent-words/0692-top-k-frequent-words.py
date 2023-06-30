from heapq import heappop, heappush, heapify
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = {}
        res = []
        maxHeap = []     
        heapify(maxHeap)
        
        for i in words:
            mp[i] = mp.get(i, 0) + 1
        
        for word, freq in mp.items():
            heappush(maxHeap, (-freq, word))
        
        for _ in range(k):
            freq, word = heappop(maxHeap)
            res.append(word)
        return res
