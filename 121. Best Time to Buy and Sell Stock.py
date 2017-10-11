class Solution(object):
    def maxProfit(self, prices):
        """
        O(n) solution
        """
        profit = 0
        minP = prices[0] if prices else None
        
        for val in prices:
            if val < minP:
                minP = val
            else:
                if val - minP > profit:
                    profit = val-minP
                    
        return profit