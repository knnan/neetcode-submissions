class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        if i >= self.size:
            raise IndexError("Index out of range")
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if i >= self.size:
            raise IndexError("Index out of range")
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

        


    def popback(self) -> int:
        item = self.arr[self.size-1]
        self.size -= 1
        return item
 

    def resize(self) -> None:
        tempArr = self.arr
        self.arr.extend([None]*self.capacity) 
        self.capacity = self.capacity * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
