# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        newNode=TreeNode(val)
        curr=root
        if curr is None:
            return newNode
        while curr != None:
            parent=curr
            if curr.val < val:
                curr=curr.right
            else:
                curr=curr.left
        if parent.val < val:
            parent.right=newNode
        else:
            parent.left=newNode
        return root
         
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        