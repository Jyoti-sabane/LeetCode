class Solution(object): 
    def isPalindrome(self, s):
        s=s.lower()
        i=0
        j=len(s)-1

        while j>i:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[j]==s[i]:
                i+=1
                j-=1
            else:
                return False
        return True
    
        """
        :type s: str
        :rtype: bool
        """
        