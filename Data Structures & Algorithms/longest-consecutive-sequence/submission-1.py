class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hs = set(nums)
        
        
        for x in nums:
            if x - 1 not in hs:
                count = 1
                while x + count in hs:
                    count += 1
                res = max(res,count)
        return res




