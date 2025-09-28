class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] == nums[i-1]:
                for j in range(i, n-1):
                    nums[j] = nums[j+1]
                n -= 1  
            else:
                i += 1
        return n
