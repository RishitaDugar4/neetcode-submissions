class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        index = 0
        
        if abs(len(s) - len(t)) > 1:
            return False 
        
        if len(s) < len(t):
            s,t = t,s

        if s and not t:
            return True

        while index < len(t): 
            if s[index] != t[index]:
                if len(s) == len(t):
                    return s[index+1:] == t[index+1:]
                else:
                    return s[index+1:] == t[index:]
            index += 1
        
        if len(s) > len(t) and s[-1] != t[-1]:
            return True 
        
        return False