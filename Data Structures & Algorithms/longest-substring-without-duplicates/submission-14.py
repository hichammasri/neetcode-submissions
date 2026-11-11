class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = {}
        l = 0
        r = 0
        maxLen = 0
        for i,c in enumerate(s):
            
            if c in lastSeen:
                l = max(lastSeen[c] + 1, l)
            curLen = r - l + 1
            maxLen = max(curLen, maxLen)
            lastSeen[c] = r
            r+=1

        return maxLen

        

            
            



        