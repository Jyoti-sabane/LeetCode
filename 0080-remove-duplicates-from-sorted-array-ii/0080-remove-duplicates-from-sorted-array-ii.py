class Solution(object):
    def removeDuplicates(self, nums):
        start1=0
        start2=1
        for i in range(2,len(nums)):
            if nums[i]!=nums[start1]:
                start1+=1
                start2+=1
                nums[start2]=nums[i]
        return start2+1

        """
        :type nums: List[int]
        :rtype: int
        """
        