class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        st = []
        n = len(heights)


        max_area = 0

        for i,h in enumerate(heights):
            while st and h < heights[st[-1]]:
                cur = st.pop()
                nse = i
                pse = st[-1] if st else -1

                area =  heights[cur] * (nse - pse - 1)
                max_area = max(max_area,area)
            st.append(i)
        
        while st:
            cur = st.pop()
            nse = n
            pse = st[-1] if st else -1

            area = heights[cur] * (nse - pse - 1)
            max_area = max(max_area,area)
        return max_area

        