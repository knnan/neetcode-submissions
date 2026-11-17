class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        idea:

        convert all anagrams to a common key,
            key can be sorted letteres or, in this case we hvae a freqSlot for 26 small case letter of english lagualge and we conver it as tuple so its hasable in a hasmmap.
            for each key of the anagram store the anagrams in a list

        """

        res = defaultdict(list)

        for s in strs:
            key = [0]*26 # dont use tuble here becuuse tuple is immutable
            for ch in s:
                key[ord(ch) - ord('a')]  += 1
            res[tuple(key)].append(s)
        
        return list(res.values())


