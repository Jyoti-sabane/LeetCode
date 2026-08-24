# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
           
    def isSymmetric(self, root):
        left=[]
        right=[]
        def preorder(root):
            if root is None:
                left.append(None)
                return 
            left.append(root.val)
            preorder(root.left)
            preorder(root.right)
            print(left)
        def postorder(root):
            if root is None:
                right.append(None)
                return 
            right.append(root.val)
            postorder(root.right)
            postorder(root.left)
            print(" ",right)
        preorder(root.left)
        postorder(root.right)

        return left==right
    
        