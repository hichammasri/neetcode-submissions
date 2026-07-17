class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_distribution = {}
        t_distribution = {}

        for c in s:
            s_distribution[c] = s_distribution.setdefault(c, 0) + 1
        
        for c in t:
            t_distribution[c] = t_distribution.setdefault(c, 0) + 1

        for c in set(list(s_distribution.keys()) + list(t_distribution.keys())):
            if s_distribution.get(c) != t_distribution.get(c):
                return False
        
        return True
        
        
        