class Solution(object):
    def addTwoNumbers(self, l1, l2):

        ans = ListNode(0)
        temp = ans
        carry = 0

        while l1 or l2:

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            total = n1 + n2 + carry

            carry = total // 10
            value = total % 10

            temp.next = ListNode(value)
            temp = temp.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            temp.next = ListNode(carry)

        return ans.next