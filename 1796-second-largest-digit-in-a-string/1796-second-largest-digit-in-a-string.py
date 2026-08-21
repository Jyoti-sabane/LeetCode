class Solution(object):
    def secondHighest(self, s):
        li=[]
        for i in range(len(s)):
            if s[i].isdigit():
                li.append(s[i])
        li=set(li)
        li=list(li)
        li.sort()
        if len(li) < 2:
            return -1
        else:
            return int(li[-2])
        

    
        """
        :type s: str
        :rtype: int
        """
        