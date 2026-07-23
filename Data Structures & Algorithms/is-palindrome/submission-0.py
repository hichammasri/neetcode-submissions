class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_norm = "".join([c for c in s if c.isalnum()]).lower()
        n = len(s_norm)
        i = 0
        j = n - 1

        while i<j:
            if s_norm[i] != s_norm[j]:
                return False
            i += 1
            j -= 1
        
        return True



        