class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

        
    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            ln = ""
            while s[l] != "#":
                ln += s[l]
                l += 1
            
            length = int(ln)
            res.append(s[l+1:l  + length + 1])
            l = l + length + 1
        return res


    # def encode(self, strs: List[str]) -> str:
    #     # res = ""
    #     # for s in strs:
    #     #     slen = len(s)
    #     #     res += f"{slen}#{s}"
    #     # return res


    # def decode(self, s: str) -> List[str]:
    #     res = []
    #     i = 0

    #     while i < len(s):
    #         j = i
    #         while s[j] != "#":
    #             j+=1
    #         length = int(s[i:j])
    #         res.append(s[ j+1 : j+1+length] )
    #         i = j+1+length
    #     return res

