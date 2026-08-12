class Solution:
    def isValid(self, s: str) -> bool:
        newmap = {"(": ")", "{": "}", "[": "]"} 
        stack = []
        for c in s:
            if c in newmap:
                stack.append(c)
                continue
            if not stack:
                return False
            if newmap[stack[-1]] != c:
                return False
            stack.pop()
        return not stack 
            