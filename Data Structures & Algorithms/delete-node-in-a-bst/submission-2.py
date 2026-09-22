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
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self.MinValNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right,minNode.val)
        return root
                


        
                

        
        