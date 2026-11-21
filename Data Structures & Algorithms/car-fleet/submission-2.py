class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = sorted([(p,s) for p,s in zip(position,speed)])
        st = []
        for p,s in pair[::-1]:
            t = (target-p)/s

            if st and st[-1] < t:


                st.append(t)
                continue
            if not st:
                st.append(t)
        return len(st)
