class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {']': '[', ')': '(', '}': '{'}

        stack = []

        for p in s:
            if p in paranthesis:
                if not stack: 
                    return False
                last = stack.pop()
                if paranthesis[p] != last:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0
        