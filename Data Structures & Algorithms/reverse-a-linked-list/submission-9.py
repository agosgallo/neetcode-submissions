# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#class Solution:
#    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#        prev = None
#        curr = head
#        while curr:
#            next = curr.next
#            curr.next = prev
#            prev = curr
#            curr = next
#        return prev

class Solution:
    def reverseList(self,head:Optional[ListNode]) -> Optional[ListNode]:
    # Caso base: lista vuota oppure un solo nodo
        if head is None or head.next == None:
            return head

    # Inverte ricorsivamente tutto ciò che viene dopo head
        new_head = self.reverseList(head.next)

    # Il nodo successivo deve ora puntare indietro verso head
        head.next.next = head

    # Elimina il vecchio collegamento head → nodo successivo
        head.next = None

    # Il nuovo inizio è quello restituito dalla ricorsione
        return new_head