class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns = []
        for i in s:
            if(i.isalnum()):
                ns.append(i)
        
        rns = list(reversed(ns))
        if rns != ns:
            return False
        else: 
            return True