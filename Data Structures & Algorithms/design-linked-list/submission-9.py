class ListNode:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index: int) -> int:
        #sanity check
        if index < 0 or index >= self.size:
            return -1
        #traversing and returning val
        i = 0
        curr = self.head    
        while i < index:
            curr = curr.next
            i +=1
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        
        new_node = ListNode(val)
        
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node

        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        
        new_node = ListNode(val)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        new_node = ListNode(val)

        if self.size == 0:
        # The new node is both head and tail
            self.head = new_node
            self.tail = new_node

        elif index == self.size:
        # Insert after the current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        else:
        # Find the node currently at index
            curr = self.head
            for _ in range(index):
                curr = curr.next

        # Insert new_node before curr
            new_node.prev = curr.prev
            new_node.next = curr

            if curr.prev is not None:
                curr.prev.next = new_node
            else:
            # Inserting at index 0
                self.head = new_node

            curr.prev = new_node

        self.size += 1  
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        if curr.prev is not None:
            curr.prev.next = curr.next
        else: #curr is the head
            self.head = curr.next
        
        if curr.next:
            curr.next.prev = curr.prev
        else: #curr is the tail
            self.tail = curr.prev

        self.size -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)