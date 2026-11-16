class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output =  defaultdict(list)


        for word in strs:
            key =  [0]*26
            for ch in word:
                key[ord(ch) - ord('a')] += 1
            output[tuple(key)].append(word)
        return list(output.values())