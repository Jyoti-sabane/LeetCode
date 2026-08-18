class Solution(object):
    def nextGreaterElements(self, nums):
        nums+=nums
        n=len(nums)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while len(stack)>0 and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(nums[i])
        return ans[:len(ans)//2]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        