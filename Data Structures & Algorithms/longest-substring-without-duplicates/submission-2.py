class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hm = {}

        if len(s) == 0:
            return 0

        l = 0
        res = 0


        for r in range(len(s)):
            if s[r] in hm and hm[s[r]] >= l:
                l = hm[s[r]] + 1
            hm[s[r]] = r
            res = max(res, r - l + 1)
        return res

        