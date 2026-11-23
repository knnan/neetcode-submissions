class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        

        count = k

        st = []
        s = num

        ans = ""
        for i in range(len(s)):
            d = s[i]
            while st and int(st[-1]) > int(d):
                st.pop()
                count -= 1

                if count == 0:
                    for e in s[i:]:
                        st.append(e)
                    break;  
            if count == 0:
                break


            st.append(d)
        while st and count:
            st.pop()
            count -= 1

        i = 0 

        while i < len(st):
            if int(st[i]) != 0:
                ans = "".join(st[i:]) 
                break
            i += 1
        return ans if ans else '0'
