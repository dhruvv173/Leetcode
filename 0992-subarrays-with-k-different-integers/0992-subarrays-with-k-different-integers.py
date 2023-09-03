class Solution:
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:

        def atmost(s, k):
            i, j, count = 0,0,0
            mp = {}
            while j < len(s):
                mp[s[j]] = 1 + mp.get(s[j], 0)


                while len(mp) > k:
                    mp[s[i]] -= 1
                    if mp[s[i]] == 0:
                        mp.pop(s[i])
                    i += 1
                count += (j-i+1)
                j += 1
            return count
    
        return atmost(s,k) - atmost(s,k-1)