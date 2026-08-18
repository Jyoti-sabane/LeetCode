class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n

        a=n-k
        nums.extend(nums[0:a])
        del nums[0:a]
        

        




        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        