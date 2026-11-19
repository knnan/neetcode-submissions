class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


            
        s1_len = len(s1)
        
        fs1 = [0] * 26
        fc = [0] * 26

        for c in s1:
            fs1[ord(c) - ord('a')] += 1


        l = 0
        for r in range(len(s2)):
            fc[ord(s2[r]) - ord('a')] += 1



            while r - l + 1 == s1_len:
                
                if tuple(fs1) == tuple(fc):
                    return True
                fc[ord(s2[l]) - ord('a')] -= 1

                l += 1
        return False
            
    """
    s1 = "ab"
    s2 = "lecabee"

    [a:1, b:1]

    iter   |    fc                  | l  | r   | wind
    1           [l: 1]                 0    0     [l]
    2         [l:1,e: 1]                0   1       [l,e]  -> checks fails -> l -=1 = 1 and fc[l] -= 1
    3          [e: 1,c:1 ]                   1    2      [e,c]

                [c: 1, a: 1]                   2   3  [c,a]
                [a1, b 1]
    """
            


        