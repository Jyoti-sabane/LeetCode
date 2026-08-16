# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution(object):
    def isPalindrome(self, head):
        values=[]
        curr=head
        while curr!=None:
            values.append(curr.val)
            curr=curr.next
        rev=values[::-1]
        return rev==values

    
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        