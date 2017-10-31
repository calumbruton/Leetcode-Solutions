class Solution(object):
    def findDisappearedNumbers(self, nums):
        """O(1) additional space solution
        Take each value and make that values index location negative
        By using absolute we can do this for every number without worrying 
        that we have changed values to negative
        We then return a list of the indices of every non-negative number
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]   
        
        
        """Better O(n) additional space solution
        p = set([i for i in range(1,len(nums)+1)])
        for num in nums:
            if num in p:
                p.remove(num)
        return list(p)
        """
        
        """The O(n) additional space easy solution
        x = set()
        n = len(nums)
        for num in nums:
            if num not in x:
                x.add(num)
        return [num for num in range(1,n+1) if num not in x]        
        """
        