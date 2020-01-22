class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        happy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                happy += customers[i]
                customers[i] = 0
        
        best, extra, b, e = 0, 0, 0, 0
        for i in range(len(customers)):
            extra += customers[i]
            if i >= X:
                extra -= customers[i-X]
            if (extra > best):
                best, b, e = extra, i, i-X
                
        happy += best
        return happy
