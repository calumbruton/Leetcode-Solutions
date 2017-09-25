class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid = []
        total = 0
        for x in ops:
            if x == "C":
                # Pop the last valid entry off the stack and remove it from sum
                y = valid.pop()
                total -= y
                
            elif x == "D":
                y = valid[-1]*2
                valid.append(y)
                total += y
            
            elif x == "+":
                l = len(valid)
                s = sum(valid[(l-2):l])
                valid.append(s)
                total += s
            
            else:
                x = int(x)
                valid.append(x)
                total += x
        
        return total