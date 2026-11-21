class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
            return
        self.minstack.append( min(self.minstack[-1],val) )
        

    def pop(self) -> None:

        val = self.stack.pop()
        self.minstack.pop()
       
        

    def top(self) -> int:
        if not self.stack:
            return False
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return False
        return self.minstack[-1]

        
