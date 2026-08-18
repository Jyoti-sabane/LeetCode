class Solution(object):
    def maxArea(self, height):
        n=len(height)
        start=0
        end=n-1
        water=0

        while start < end:
            width=end-start
            curr_water=min(height[start],height[end])*width
            water=max(water,curr_water)
            if height[end] < height[start]:
                end-=1
            else:
                start+=1
        return water
            


        """
        :type height: List[int]
        :rtype: int
        """
        