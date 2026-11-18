class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            

            l = i + 1
            r  = n -1 
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i], nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
        return res














        def old():


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
                    

