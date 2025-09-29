class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        i=0
        while i < len(s)-1:
            if roman[s[i+1]] > roman[s[i]]:
                total+= roman[s[i+1]] - roman[s[i]]
                i+=2
            else:
                total+= roman[s[i]]
                i+=1
        if i == len(s) - 1:   
            total += roman[s[i]]
        return total
            
