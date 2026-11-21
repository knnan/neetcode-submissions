class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        closeToOpen = {
            '}': '{',
            ']':'[',
            ')' : '('
        }


        for i, ch in enumerate(s):

            if ch in closeToOpen:

                if not st or closeToOpen[ch] != st[-1]:
                    return False
                else:
                    st.pop()
                
            else:
                st.append(ch)
        return not st

