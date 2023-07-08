class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        '''
        - exactly similar to LC424: Longest repeating character replacement
        - https://leetcode.com/problems/longest-repeating-character-replacement/description/
        '''     
        count, res = {}, 0
        l, r = 0,0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
        '''
        Optimized approach, difficult to make out
        count, res, l, r, maxf = {}, 0, 0, 0, 0
        while r < len(arr):
            count[arr[r]] = 1 + count.get(arr[r], 0)
            maxf = max(maxf, count[arr[r]])

            while (r-l+1) - maxf > k:
                count[arr[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
        '''