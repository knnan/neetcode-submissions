class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """
        r 0 -> len(nums)
        add to cur sum 

        if cur_sum >= target:
            calculate new min_len of subarr
            incremant left pointer



        """
        
        l = 0
        min_len = float("inf")
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                min_len = min(min_len,r-l+1)
                window_sum -= nums[l]
                l += 1
        return 0 if math.isinf(min_len) else min_len
            