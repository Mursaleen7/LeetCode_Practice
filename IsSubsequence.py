class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        
        if s == "":
            return True
        
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1
            j += 1

        if i==len(s):
            return True
        else:
            return False
        

    
