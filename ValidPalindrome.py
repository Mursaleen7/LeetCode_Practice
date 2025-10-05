class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        noSpace = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        i=0
        j=len(noSpace)-1
        if i == j:
            return True
        output=True
        while i<j:
            if noSpace[i] == noSpace[j]:
                output=True
                i+=1
                j-=1
            else:
                return False
        return output
