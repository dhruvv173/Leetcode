class Solution(object):
    def combine(self, n, k):
        res = []
        def dfs(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return 
            for j in range(i, n + 1):
                curr.append(j)
                dfs(j+1, curr)
                curr.pop()

        dfs(1,[])
        return res