class Solution(object):
    def isSubsequence(self, s, t):
        n=len(s)
        li=[False]*n
        i=0
        j=0
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                li[i]=True
                i+=1
                j+=1
            else:
                j+=1
        return all(li)



        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        