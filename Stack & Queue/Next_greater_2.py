class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #not the optimal solution
        # lis = [-1] * len(nums)
        # nums2 = nums *2
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums2)):
        #         if nums2[j] > nums[i]:
        #             lis[i] = nums2[j]
        #             break
        # return lis
        
        '''optimal solution'''
        
        stack = []
        output = [-1] * len(nums)
        
        nums2 = nums * 2
        
        for i in range(len(nums2)):
            while stack and stack[-1][0] < nums2[i]:
                val, pos = stack.pop()
                output[pos] = nums2[i]
            if i < len(nums):
                stack.append((nums2[i],i))
                
        return output