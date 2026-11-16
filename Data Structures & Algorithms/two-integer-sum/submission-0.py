class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,val in enumerate(nums):
            pair = target - val
            if pair in hashmap:
                return [hashmap[pair],i]
            hashmap[val] = i
        