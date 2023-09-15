class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, n+2, n+3]
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1, rob2 = rob2, tmp

        return rob2