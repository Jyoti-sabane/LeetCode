class Solution(object):
    def lengthOfLongestSubstring(self, s):
        li = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in li:
                li.remove(s[left])
                left += 1

            li.add(s[right])
            ans = max(ans, right - left + 1)

        return ans

        