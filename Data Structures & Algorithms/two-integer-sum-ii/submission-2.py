class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        idea:
            use two pointers at opp end
            if sum of the two pinte elems is < increaet lo to incresae the sum else decre hi to decrese the sum , 

            time: o(n), we check each elemnt only once
            space: o(1) we dont use any extra space
        """
        lo = 0

        hi = len(numbers) - 1

        while lo < hi:
            cur = numbers[lo] + numbers[hi]
            if cur == target:
                return [lo+1,hi+1]
            elif cur < target:
                lo += 1
            else:
                hi -= 1
        
        