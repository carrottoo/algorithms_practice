#  a min_stack that supports push, pop, top, and retrieving the minimum element in constant time (O(1) time complexity)

class MinStack:

    def __init__(self):
        self.data = []
        self.min = []
        

    def push(self, val: int) -> None:
        if len(self.data) == 0 :
            self.min.append(val)
        elif self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
            
        self.data.append(val)
        


    def pop(self) -> None:
        self.data.pop(- 1)
        self.min.pop(-1)
        

    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.min[-1]