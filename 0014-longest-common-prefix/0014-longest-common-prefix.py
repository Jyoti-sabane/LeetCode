class Solution(object):
    def longestCommonPrefix(self, strs):
        ans=strs[0]
        for i in range(1,len(strs)):
            temp=""
            for j in range (min(len(strs[i]),len(ans))):
                if ans[j]!=strs[i][j]:
                    break
                temp+=ans[j]
            ans=temp
        return ans


        """
        :type strs: List[str]
        :rtype: str
        """
        