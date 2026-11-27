class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = m = 0
        r = len(nums) - 1

        while   m <= r:
            val = nums[m]
            if val == 0:
                
                nums[l],nums[m] = nums[m],nums[l]
                l += 1
                m += 1
            elif val == 2:
                nums[r],nums[m] = nums[m],nums[r]
                r -= 1
            else:
                m += 1

            
            