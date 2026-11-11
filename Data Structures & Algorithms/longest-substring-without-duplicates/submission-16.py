class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        l = 0
        r = 0
        maxLen = 0
        for r in range(len(s)):
            if s[r] in lastSeen:
                l = max(lastSeen[s[r]] + 1, l)
            maxLen = max(r - l + 1, maxLen)
            lastSeen[s[r]] = r
        return maxLen

        

            
            



        