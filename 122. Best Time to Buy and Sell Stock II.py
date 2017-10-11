class Solution(object):
    def maxProfit(self, prices):
        
        """Much more concise O(n) solution using list comprehension"""
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
        
        
        
        
        """
        O(n) solution that minimizes the number of transactions to maximimize profit and minimize
        trading costs
        
        profit = 0
        min_loc = 0 if prices else None
        high_loc = 0
        bought = False
        
        for i, price in enumerate(prices):
            # if greater than the last number increase high
            if price > prices[i-1]:
                high_loc = i
                bought = True 
                
            if price < prices[i-1]:
                if bought: 
                    profit += prices[high_loc] - prices[min_loc]
                    bought = False
                min_loc = i
                
        if bought: 
            profit += prices[high_loc] - prices[min_loc]
        return profit
        """