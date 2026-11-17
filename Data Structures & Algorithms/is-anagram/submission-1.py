class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        create a count of characters in s : freqS
        for elem in t redue the count  in freqS[elem] by 1
        if after reducint count is < 0: it is not anagram
        

        """

        if len(s) != len(t):
            return False

        freqS = Counter(s)
        for ch in t:
            freqS[ch] -= 1
            if freqS[ch] < 0:
                return False
        return True
        
        
        