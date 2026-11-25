class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        st = []

        """
        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        p_s  [(0-1, 1-2, 4-2 ,7-1]
        t = [10/1,9/2,6/2,3/1] = [10,4.5,3,3]

        1 -> st = [10]
        2 -> 5 < = st[-1] =>10 => True contnue
        3 -> 5 
        4 -> 10 

        """

        p_s = sorted([ i for i in zip(position,speed)])
        time = [ (target- i[0])/i[1] for i in p_s]
        for t in time[-1::-1]:
            
            if st and t <= st[-1]:
                continue
                

            st.append(t) 
        return len(st)