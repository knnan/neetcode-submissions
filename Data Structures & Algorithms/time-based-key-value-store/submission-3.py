class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        
        arr = self.hm[key]

        l = 0
        r = len(arr) - 1
        res = ""
        while l<=r:

            m = (l+r)//2
            t,val= arr[m]
            if t <= timestamp:
                res = val
                l = m + 1
            
            else:
                r = m - 1
        return res       

        
