class Solution(object):
    def threeSum(self, nums):
        i=0
        j=1
        k=len(nums)-1
        s=0
        nums.sort()
        li=[]
        while i < k-1:
            if j >= k:
                i+=1
                while i < k-1 and nums[i] == nums[i-1]:
                    i+=1
                j=i+1
                k=len(nums)-1
                continue 
                
            s=nums[i]+nums[j]+nums[k]
            
            if s < 0:
                j+=1
            elif s > 0:
                k-=1
            else:
                ans=[nums[i],nums[j],nums[k]]
                if ans not in li:
                    li.append(ans)
                
                while j < k and nums[j] == nums[j+1]:
                    j+=1
                while j < k and nums[k] == nums[k-1]:
                    k-=1
                    
                j+=1
                k-=1
        return li
