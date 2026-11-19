class Solution:
    def minWindow(self, s: str, t: str) -> str:

        freqT = Counter(t)

        l = 0

        output = ""

        freqC = Counter()

        need = len(freqT)
        have = 0

        for r in range(len(s)):
            if s[r] in freqT:
                freqC[s[r]] += 1

                if freqT[s[r]] == freqC[s[r]]:
                    have += 1
            


            while have == need:

                
                if output == ""  or (r - l + 1) < len(output) :
                    output = s[l:r+1]
                if s[l] in freqT:
                    freqC[s[l]] -= 1
                    if freqC[s[l]] < freqT[s[l]]:
                        have -= 1

                l += 1
                
        return output
