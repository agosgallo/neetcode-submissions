# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #since all the values smaller than the root are on the left we just take the left-most element
    def MinValNode(self,root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self,root,key):
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        #here we found the element
        else:
            #here it has no child or has just one so it sufficies to substitute it with the child
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            #here it has 2 children so we need to change the current node with the minimum value on it's right so to preserve all the characterics of the BTS
            else:
                #search the min node starting from right wich are all bigger than the root
                minNode = self.MinValNode(root.right)
                #we change the value with the one found of the root node
                root.val = minNode.val
                #here we remove the minNode from it's current position
                root.right = self.deleteNode(root.right,minNode.val)
        return root 
                


        
                

        
        