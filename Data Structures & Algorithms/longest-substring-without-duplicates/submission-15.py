class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        l = 0
        r = 0
        maxLen = 0
        while r<len(s):
            if s[r] in lastSeen:
                l = max(lastSeen[s[r]] + 1, l)
            curLen = r - l + 1
            maxLen = max(curLen, maxLen)
            lastSeen[s[r]] = r
            r+=1
        return maxLen

        

            
            



        