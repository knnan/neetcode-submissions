class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buc = [[] for _ in range( len(nums) + 1)] # +1 because len(nums) also resul in index 0 - 999 if len(nums) =  1000 we need index value of 1000

        freq = Counter(nums)

        for x,cnt in freq.items():
            buc[cnt].append(x)
        
        for b in buc[::-1]:
            while b and len(res) < k:
                res.append(b.pop())
            if len(res) == k:
                return res








        def old():
        
            """
            create a freq count of elemts in nums
            
            counting bucket where index is the freq and val is the ele
            add itsm from freq_count to bucket 
            iterate through the bucket in reverse until u fild elemts in bucket 
            push ele into res until the no of ele pushed == k

            complexity analysis:
            time: o(n)
            space: o(n)


            """

            buckets = [[] for _ in range(len(nums) + 1)]

            freq = Counter(nums)

            for val,count in freq.items():
                buckets[cnt].append(val)

            res = []

            for b in buckets[::-1]:
                for val in b:
                    res.append(val)
                    if len(res) == k:
                        return res
                