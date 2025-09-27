class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num = float('inf')
        i = 0
        while i < len(prices):
            j = i
            while j < len(prices):
                diff = prices[i] - prices[j]
                if diff < num and diff < 0:
                    num = diff
                j += 1
            i += 1
        if num == float('inf'):
            num = 0
        return -num

