class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l=0
        r=len(height)-1
        w=0
        while l < r:
            if height[l]<=height[r]:
                number=height[l]* (r-l)
                l+=1
            elif height[l]>height[r]:
                number=height[r]* (r-l)
                r-=1
            if number > w:
                w=number
                
        return w
            
