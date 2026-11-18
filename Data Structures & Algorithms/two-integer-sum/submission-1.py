class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i,x in enumerate(nums):
            pair = target - x
            if pair in hm:
                return [hm[pair],i]
            hm[x] = i








        def old():
            hashmap = {}

            for i,val in enumerate(nums):
                pair = target - val
                if pair in hashmap:
                    return [hashmap[pair],i]
                hashmap[val] = i
            