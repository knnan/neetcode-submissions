class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = r

        def canEat(k):
            
            return totalHours
                
        


        while l <= r:
            k = (l+r) // 2
            


            totalHours = 0
            for p in piles:
                totalHours += math.ceil(p/k)

            if totalHours <= h:
                min_k = min(min_k,k)
                r = k - 1
            elif totalHours > h:
                l = k + 1
        return min_k



