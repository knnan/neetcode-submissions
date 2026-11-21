class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1,-1):

            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if not st:
                output[i] = 0
            else:
                output[i] = st[-1] - i
            
            st.append(i)
        return output
        