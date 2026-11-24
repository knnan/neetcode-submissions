class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pivot = None

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l =  m + 1
        
        pivot = l

        def binary_search(left,right):
            while left <= right:
                mid = (left+right) // 2
                val = nums[mid]
                if val == target:
                    return mid
                elif val < target:
                    left =  mid  + 1
                else:
                    right = mid - 1
            return -1


        if pivot == 0 or target <= nums[-1]:
            return binary_search(pivot,len(nums) - 1)
        else:
            return binary_search(0,pivot - 1)



        
        