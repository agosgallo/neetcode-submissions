class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:

        new_node = ListNode(url)
        # Connect new_node backward
        new_node.prev = self.current
        # Connect the current node forward
        self.current.next = new_node
        # Move current to new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        # Move backward while:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        # 1. steps is greater than zero
        # 2. a previous node exists
        # Return the value stored in the current node

    def forward(self, steps: int) -> str:
        # Move current toward the next node
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -=1
        return self.current.val
        # Decrease steps

    # Return the current URL
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)