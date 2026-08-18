class Solution(object):
    def removeElement(self, nums, val):
        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 <= ptr2:
            if nums[ptr2] == val:
                ptr2 -= 1
            elif nums[ptr1] == val and nums[ptr2]!=val:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
                ptr2 -= 1
            else:
                ptr1 += 1
        return ptr2 + 1
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        