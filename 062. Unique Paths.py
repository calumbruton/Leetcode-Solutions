class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """DP Solution O(m+n) time"""

        uniqueRoots = {}
        # Fill the right column with 1's as each only has one unique path
        for i in range(m,0,-1):
            uniqueRoots[(i,n)] = 1
          
        # Fill the bottom column with 1's as each only has one unique path
        for i in range(n,0,-1):
            uniqueRoots[(m,i)] = 1
        
         # Fill every other square using the sum of the unique paths of the squares to its left and right
        for x in range(m-1,0,-1):
            for y in range(n-1,0,-1):
                uniqueRoots[(x,y)] = uniqueRoots[(x+1,y)] + uniqueRoots[(x,y+1)]
        
        return uniqueRoots[(1,1)]


    
        
        
        
    """
    Recursive solution. Works but times out on larger inputs. O(n^2) time complexity
    
        def uniquePaths(self, m, n):
        
        :type m: int
        :type n: int
        :rtype: int
        
        x = self.recursiveUnique(m,n)
        return x
    
    def recursiveUnique(self, m, n):
        A recursive solution that goes through every unique path
        if m > 1 and n > 1:
            return self.recursiveUnique(m-1, n) + self.recursiveUnique(m, n-1)
        elif n > 1:
            return self.recursiveUnique(m, n-1)
        elif m > 1:
            return self.recursiveUnique(m-1, n)
        else:
            return 1
    
    """