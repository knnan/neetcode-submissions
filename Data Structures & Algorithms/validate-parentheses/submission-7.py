class Solution:
    def isValid(self, s: str) -> bool:


        st = []

        closeToOpen = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        if len(s) == 0:
            return True


        for i in range(len(s)):
            ch  = s[i]
            if ch in closeToOpen:
                # if st is empty -> false
                # if st top is not open pair  -> false

                if st and st[-1] == closeToOpen[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
    
        return not st
























        # st = []

        # closeToOpen = {
        #     '}': '{',
        #     ']':'[',
        #     ')' : '('
        # }


        # for i, ch in enumerate(s):

        #     if ch in closeToOpen:

        #         if not st or closeToOpen[ch] != st[-1]:
        #             return False
        #         else:
        #             st.pop()
                
        #     else:
        #         st.append(ch)
        # return not st

