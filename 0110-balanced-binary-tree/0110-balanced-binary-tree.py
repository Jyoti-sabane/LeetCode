# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res=True
    def height(self,root):
        if root is None:
            return 0
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        if abs(leftheight-rightheight) > 1:
            self.res=False
        return max(leftheight, rightheight) + 1
    def isBalanced(self, root):
        if root is None:
            return True
        self.height(root)
        return self.res
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        