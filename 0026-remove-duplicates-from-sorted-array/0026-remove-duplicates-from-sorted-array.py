class Solution(object):
    def removeDuplicates(self, nums):
        start=0
        for i in range(1,len(nums)):
            if nums[start] != nums[i]:
                start+=1
                nums[start]=nums[i]
        return start+1


            
        """
        :type nums: List[int]
        :rtype: int
        """
        