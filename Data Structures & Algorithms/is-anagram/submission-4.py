class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        s_distribution = {}
        t_distribution = {}

        for c in s:
            s_distribution[c] = s_distribution.setdefault(c, 0) + 1
        
        for c in t:
            t_distribution[c] = t_distribution.setdefault(c, 0) + 1

        if len(t_distribution)!=len(t_distribution):
            return False

        for c in t_distribution:
            if s_distribution.get(c) != t_distribution.get(c):
                return False
        
        return True
        
        
        