class Solution(object):
    def fizzBuzz(self, n):
        """
        -- Cool one line solution --
        Multiplying a string by true or false works and (not i%5) makes the value 0 True and any other 
        number return False. Because 0 represents True and any other number represents false
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
        """
        r = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                r.append("FizzBuzz")
            elif i%3 == 0:
                r.append("Fizz")
            elif i%5 == 0:
                r.append("Buzz")
            else:
                r.append(str(i))
        
        return r
        