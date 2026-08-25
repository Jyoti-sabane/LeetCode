import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        ans=heapq.nlargest(k,nums)
        return ans[-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        