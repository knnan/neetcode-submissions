class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        nums=[1,2,3,4,5,6,7]
        k=3

        6,7,1,2,3,4,5
        """
        
        def rev(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        n = len(nums)
        
        k = k % n

        if not k:
            return

        rev(0,n - 1)
        rev(0,k - 1)
        rev(k,n - 1)
     