class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        dict1={}
        for i in range(n):
            rem=target-nums[i]
            if rem in dict1:
                return [i,dict1[rem]]
            dict1[nums[i]]=i




            
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        