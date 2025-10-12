class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        stack = []
        matching = {')': '(', '}': '{', ']': '['}
        
        while i < len(s):
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] in ')}]':
                if not stack:  
                    return False
                if stack.pop() != matching[s[i]]:  
                    return False
            i += 1
        
        return len(stack) == 0  
