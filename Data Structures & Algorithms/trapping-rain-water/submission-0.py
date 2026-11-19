class Solution:
    def trap(self, height: List[int]) -> int:

        output = 0
        left_max = [-1] * len(height)
        right_max = [-1] * len(height)

        left_prefix = 0
        for i,h in enumerate(height):
            left_max[i] = left_prefix
            left_prefix = max(left_prefix,height[i])

        right_prefix = 0
        for i in range(len(height) -1, -1,-1):
            right_max[i] = right_prefix
            right_prefix = max(right_prefix,height[i])

        
        for i,h in enumerate(height):

            water_height = min(left_max[i],right_max[i]) - height[i]
            water_amt = 0 if water_height < 0 else water_height
            output += water_amt
        return output


        
