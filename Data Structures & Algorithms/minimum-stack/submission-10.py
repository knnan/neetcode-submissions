class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
        
    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minst:
            cur_min = min(self.minst[-1],val)
            self.minst.append(cur_min)
            return
        self.minst.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()
    
    def top(self) -> int:
        if self.st:
            return self.st[-1]
        else:
            return False

    def getMin(self) -> int:
        return self.minst[-1]
        



