https://leetcode.com/problems/sliding-window-maximum/description/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Brute force approach O(n^2)
        # ans = []
        # for i in range(len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        # return ans
        # TLE for huge inputs
        i = j = 0
        lst = deque()
        ans = []

        while j < len(nums):
            while lst and lst[-1] < nums[j]:
                lst.pop()
            lst.append(nums[j])

            if j - i + 1 < k:
                j += 1
            
            elif j - i + 1 == k:
                ans.append(lst[0])
                if nums[i] == lst[0]:
                    lst.popleft()
                i += 1
                j += 1
        return ans