class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2] -> after sort

        a + b + c = 0
        a = -(b+c)
        b+c = -a

        for a i need to find two sum whoser targe is -(a)



        """
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            # handle duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue # dont incremnt i inside a for loop as it gets reset

            lo = i+1
            hi = len(nums) - 1

            while lo < hi:

                cur_sum = nums[i] + nums[lo] + nums[hi]

                if cur_sum < 0:
                    lo +=1
                elif cur_sum > 0:
                    hi -= 1
                elif cur_sum == 0:
                    res.append([nums[i],nums[lo],nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    hi -= 1
        return res
                

