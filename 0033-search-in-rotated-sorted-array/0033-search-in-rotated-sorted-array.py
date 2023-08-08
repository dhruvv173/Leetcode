class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2             
            if target == nums[mid]:      
                return mid
            
            #check the left sorted portion of the array
            if nums[l] <= nums[mid]:             #if true this means that the target is in the left sorted portion
                if target > nums[mid] or target < nums[l]:        #check both the conditions for the target and adjust the left pointer accordingly
                    l = mid + 1
                else:
                    r = mid - 1
            else:                                               
                if target < nums[mid] or target > nums[r]:  
                    r = mid - 1
                else:
                    l = mid + 1
        return -1                