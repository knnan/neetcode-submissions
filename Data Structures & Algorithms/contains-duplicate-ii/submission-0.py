class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        hm = {}

        for i,x in enumerate(nums):

            if x in hm:
                if abs(hm[x]-i) <= k:
                    return True
            hm[x] = i
        return False 

        