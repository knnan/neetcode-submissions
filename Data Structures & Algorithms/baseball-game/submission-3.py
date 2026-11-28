class Solution:
    def calPoints(self, operations: List[str]) -> int:

        st = []
        cur_sum = 0
        for ch in operations:
            if ch == "+" and len(st) >= 2:
                b = int(float(st[-1]))
                a = int(float(st[-2]))
                val = a+b
                cur_sum += val
                st.append(str(val))
                
            elif ch == "D" and st:
                prev_score = int(float(st[-1]))
               
                val = prev_score*2
                st.append(str(val))
                cur_sum += val

            elif ch == "C" and st:
                val = st.pop()
                cur_sum -= int(float(val))
            else:
                st.append(ch)
                cur_sum += int(float(ch))
        return cur_sum

        