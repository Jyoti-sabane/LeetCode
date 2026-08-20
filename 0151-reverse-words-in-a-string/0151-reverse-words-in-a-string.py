class Solution(object):
    def reverseWords(self, s):
        li=s.split()
        rev=" ".join(reversed(li))
        return rev
        """
        :type s: str
        :rtype: str
        """
        