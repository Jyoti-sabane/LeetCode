from collections import deque
class MyQueue(object):

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, x):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        """
        :type x: int
        :rtype: None
        """
        
    def pop(self):
        if self.empty():
            return True
        return self.stack1.pop()
        """
        :rtype: int
        """
    def peek(self):
        return self.stack1[-1]
        """
        :rtype: int
        """  
    def empty(self):
        return len(self.stack1)==0
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()