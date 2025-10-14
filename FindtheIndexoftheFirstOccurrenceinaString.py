class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        i = 0
        k = 0
        count = 0
        index = 0

        while i < len(haystack):
            if k < len(needle) and haystack[i] == needle[k]:
                if count == 0:
                    index = i  
                count += 1
                k += 1
            else:
                if count > 0:
                    i = index  
                count = 0
                k = 0

            if count == len(needle):
                return index

            i += 1

        return -1
