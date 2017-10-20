import operator
class Solution(object):
    
    def diffWaysToCompute(self, input):
        """
        Divide and conquer algorithm
        """
        ops = { "+": operator.add, "-": operator.sub, "*": operator.mul}
        if input.isdigit():
            return [int(input)]
        retNums = []
        for i,c in enumerate(input):
            if c in '+-*':
                # Get the values from the left and right side using divide and conquer
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                for x in l:
                    for y in r:
                        retNums.append(ops[c](int(x),int(y)))
        
        return retNums