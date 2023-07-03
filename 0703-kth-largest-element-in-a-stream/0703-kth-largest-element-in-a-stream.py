class KthLargest(object):
    def __init__(self, k, nums):
        #minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapify(self.minHeap)
        while len(self.minHeap) > k:
            heappop(self.minHeap)

        
    def add(self, val):
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)