class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if n<=2:
            return n
        start1=0
        start2=1
        for i in range (2,n):
            if nums[start1]!=nums[i]:
                start1+=1
                start2+=1
                nums[start2]=nums[i]
        return start2+1


        """
        :type nums: List[int]
        :rtype: int
        """
        