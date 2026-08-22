# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self._items=[]
    
    def is_empty(self):
        return len(self._items)==0

    def enqueue(self,item):
        self._items.append(item)
    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self._items.pop(0)
    def peek(self):
        if self.is_empty():
            return "queue is empty"
        return self._items[0]
    def size(self):
        return len(self._items)
class Solution(object):
    def averageOfLevels(self, root):
        queue=Queue()
        ans=[]
        if root != None:
            ans.append(root.val)
        else:
            return ans
        queue.enqueue(root)
        while queue.size()>0:
            level=[]
            for i in range(queue.size()):
                front=queue.dequeue()
                if front.left != None:
                    queue.enqueue(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.enqueue(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                s=sum(level)
                n=float(len(level))
                avg=s/n
                ans.append(avg)
        return ans

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
