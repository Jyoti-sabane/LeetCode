# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head
        hasCycle=False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                hasCycle= True
                break
        if not hasCycle:
            return None
        
        l=1
        while slow.next!=fast:
            slow=slow.next
            l+=1
        slow=slow.next

        fast=head
        slow=head
        for i in range (l):
            fast=fast.next
        while slow!=fast:
            fast=fast.next
            slow=slow.next 
        return slow
        
        
        return False
        """
        :type head: ListNode
        :rtype: ListNode
        """
        