class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                j += 1
                ans = max(ans, j)
            else:
                j = 0
        return ans