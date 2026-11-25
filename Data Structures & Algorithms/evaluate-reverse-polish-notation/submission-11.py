class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands="+-*/"

        st = []
        
        for t in tokens:
            if t in operands:
                b = int(float(st.pop()))
                a = int(float(st.pop()))
                match t:
                    case "+":
                        val = a + b
                        st.append(str(val))
                    case "-":
                        val = a - b
                        st.append(str(val))
                    case "*":
                        val = a * b
                        st.append(str(val))
                    case "/":
                        val = a / b
                        st.append(str(val))
            else:
                st.append(t)
        return int(float(st[-1]))

        


