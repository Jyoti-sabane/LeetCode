class Solution(object):
    def isValid(self, s):
        n=len(s)
        stack=[]
        if n%2!=0:
            return False
        for ch in list(s):
            if ch=="(" or ch=="[" or ch=="{":
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False 
                top=stack.pop()
                if ch==")" and top!="(":
                    return False
                elif ch=="]" and top!="[":
                    return False
                elif ch=="}" and top!="{":
                    return False
        if len(stack)==0:
            return True
        return False

        
        """
        :type s: str
        :rtype: bool
        """
        