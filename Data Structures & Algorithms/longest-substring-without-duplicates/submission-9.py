class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        l = 0
        r = 0
        maxLen = 1
        while r<len(s):
            if s[r] in seen:
                while s[l]!=s[r]:
                    seen.remove(s[l])
                    l+=1
                l+=1
            curLen = r - l + 1
            maxLen = max(curLen, maxLen)
            seen.add(s[r])
            r+=1

        return maxLen

        

            
            



        