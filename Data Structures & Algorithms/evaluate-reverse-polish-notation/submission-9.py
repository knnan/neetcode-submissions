class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        output = 0
        operators = ["+","-","*","/"]

        def convert(val):
            try:
                return int(val)
            except ValueError:
                return int(float(val))

        for t in tokens:

            if t in operators:
                right = convert(st.pop())
                left = convert(st.pop())
                val = 0
                if t == "+":
                    val = left + right
                elif t == "-":
                    val = left - right
                elif t == "*":
                    val = left * right
                else:
                    val = left / right
                st.append(str(val))
                output = val
            else:
                st.append(t)
        return convert(st[-1])
        