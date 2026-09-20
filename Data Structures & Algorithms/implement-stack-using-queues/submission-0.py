class MyStack:

    def __init__(self):
        self.stack = []
        self.size = 0
    
        

    def push(self, x: int) -> None:

        self.stack.append(x)
        self.size +=1
        

    def pop(self) -> int:
        if self.stack:
            removed = self.stack[self.size-1]
            self.stack.pop(self.size-1)
            
        self.size -=1
        return removed
        

    def top(self) -> int:
        if self.stack:
            return self.stack[self.size - 1]
        else:
            return None
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()