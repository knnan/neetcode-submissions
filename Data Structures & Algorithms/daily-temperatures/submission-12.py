class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        st = []



        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:                
                j = st.pop()
                no_of_days = i - j
                result[j] = no_of_days
            st.append(i)
        return result
        