class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        numsIdx = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = numsIdx[val]
                res[idx] = curr
            if curr in numsIdx:
                stack.append(curr)
        return res    
        
        #Not the optimal solution time-O(n*m) space-O(n)
#         numsIdx = {n:i for i,n in enumerate(nums1)}
#         res = [-1] * len(nums1)
        
#         for i in range(len(nums2)):
#             if nums2[i] not in numsIdx:
#                 continue
#             for j in range(i+1, len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     idx = numsIdx[nums2[i]]
#                     res[idx] = nums2[j]
#                     break
#         return res
