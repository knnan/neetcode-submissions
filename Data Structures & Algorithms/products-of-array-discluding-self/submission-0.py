class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]

        left_prefix = [1,1,2 8]
        right_prefix = [48,24,6,1]


        """
        n = len(nums)
        left = [0] * n
        right = [0] * n
        res = [0] * n
        prefix = 1
        for i in range(len(nums)):
            left[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums) - 1,-1,-1):
            right[i] = suffix
            suffix = suffix * nums[i]

        for i in range(n):
            res[i] = left[i] * right[i]
        return res




        