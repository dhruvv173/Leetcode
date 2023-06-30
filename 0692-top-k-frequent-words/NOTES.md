use maxHeap as we have to return the answer in the lexographical order.
maxHeap reason: This way, the elements with higher frequency will have higher priority in the heap. In case of a tie in frequency, the lexicographical ordering of the words will be automatically maintained because tuples are compared lexicographically.
​
If the condition is changed to return the answer in any order, use minHeap
```
from heapq import heappop, heappush, heapify
class Solution:
def topKFrequent(self, words: List[str], k: int) -> List[str]:
mp = {}
res = []
minHeap = []
heapify(minHeap)
for i in words:
mp[i] = mp.get(i, 0) + 1
for word, freq in mp.items():
heappush(minHeap, (freq, word))
if len(minHeap) > k:
heappop(minHeap)
while minHeap:
res.append(heappop(minHeap)[1])
return res
```