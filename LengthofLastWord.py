class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i=len(s)-1
        count=0

        while i>=0:
            if s[i]!=" ":
                count+=1
            if s[i]==" " and count>0:
                return count
            i-=1
        return count
