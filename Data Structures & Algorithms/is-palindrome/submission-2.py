class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = [c.lower() for c in s if c.isalnum()]
        print(s_clean)
        return s_clean == s_clean[::-1]

        