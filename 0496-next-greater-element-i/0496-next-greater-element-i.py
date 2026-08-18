class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums2)
        stack=[]
        ans={}
        for i in range (n-1,-1,-1):
            while len(stack)>0 and nums2[i]>=stack[-1]:
                stack.pop()
            if len (stack)==0:
                ans[nums2[i]]=-1
            else:
                ans[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        res=[]
        for i in nums1:
            res.append(ans[i])
        return res



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        