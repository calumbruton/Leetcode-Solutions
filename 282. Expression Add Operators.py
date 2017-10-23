class Solution(object):
    def addOperators(self, num, target):
        """
        not accepted because it does not account for the input "105" with target 5
        having the posibility of "10-5"
        """
        n = len(num)
        if n == 0: return []
        
        # valid cominations are the combinations of operands that work
        validCombos = []
        
        ops = {"+":operator.add, "-":operator.sub, "*":operator.mul }
        
        # Create an array of every combination of n-1 operands
        combinations = []
        for op in itertools.product("+-*", repeat=n-1):
            combinations.append(op)
        
        # Seperate each number in the string
        nums = []
        for operand in num:
            nums.append(int(operand))

        # For each combination of operators
        for combination in combinations:
            operands = [x for x in nums]
            operators = [x for x in combination]
            
            # Work through each pair of operands that use multiplication
            # Pop the i position operator, and use it on the i and i+1 position operand
            # Remove the i+1 position operand and store the result in the i position
            remaining_ops = len(operators)
            i = 0
            while i < remaining_ops:
                if operators[i] in ['*']:
                    second = operands.pop(i+1)
                    operands[i] = ops[operators.pop(i)](operands[i],second)
                    remaining_ops -= 1
                else:
                    i += 1
            
            # Work through each pair of operands that do not use multiplication
            i = 0
            while i < remaining_ops:
                if operators[i] in ['+', '-']:
                    second = operands.pop(i+1)
                    operands[i] = ops[operators.pop(i)](operands[i],second)
                    remaining_ops -= 1
                else:
                    i += 1
            
            # If the final value is equal to target add it to the valid combos
            if operands[-1] == target:
                result = [x for pair in zip(num, combination) for x in pair]
                result.append(num[-1])
                result = ''.join(result)
                validCombos.append(result)
        
        return validCombos
    
    
            
        
        
        """
            for x in range(len(operators)):  
                last = operands.pop()
                operands[-1] = ops[operators.pop()](operands[-1],last)
            """