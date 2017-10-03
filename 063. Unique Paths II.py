class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """DP Solution O(m+n) time
        
        Method 1: 
        Solve by using tabulation 
        """
        
        m = len(obstacleGrid)       # num rows
        n = len(obstacleGrid[0])    # num cols
        uniqueRoots = {}            # Dict holding the unique roots from a square - keys as tuple - using 1 as first index

        
        # Wherever there is a 1 in the input matrix enter a 0 for that location in the unique roots Dict
        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y] == 1:
                    uniqueRoots[(x+1,y+1)] = 0
        
        print (uniqueRoots) 
        
        # Fill the right column with 1's as each only has one unique path
        SeenObstacle = False
        for i in range(m,0,-1):
            # If an obstacle is seen change the corresponding Boolean
            if (i,n) in uniqueRoots:
                SeenObstacle = True
                print ((i,n), 'Was in uniqueRoots')
                
            # If there has not been an obstacle in the row make the value 1
            if not SeenObstacle:
                uniqueRoots[(i,n)] = 1
                
            # Else the value is 0
            else:
                uniqueRoots[(i,n)] = 0
          
        # Fill the bottom row with 1's as each only has one unique path
        if obstacleGrid[m-1][n-1] != 1: del uniqueRoots[(m,n)]
        SeenObstacle = False
        for i in range(n,0,-1):
            # If an obstacle is seen change the corresponding Boolean
            if (m,i) in uniqueRoots:
                SeenObstacle = True
                print ((m,i), 'Was in uniqueRoots')
                
            # If there has not been an obstacle in the row make the value 1
            if not SeenObstacle:
                uniqueRoots[(m,i)] = 1
                
            # Else the value is 0
            else:
                uniqueRoots[(m,i)] = 0
        
         # Fill every other square using the sum of the unique paths of the squares to its left and right
        for x in range(m-1,0,-1):
            for y in range(n-1,0,-1):
                if (x,y) not in uniqueRoots:
                    uniqueRoots[(x,y)] = uniqueRoots[(x+1,y)] + uniqueRoots[(x,y+1)]
        
        return uniqueRoots[(1,1)]
        
        
        
        
        """
        Method 2:
        Use for loop r recursion to find paths and from each index store the number of unique paths from there
        So each time we try and find another path if we get to a node with stored vals we don't need to
        recurse down it again we can just pull the unique values that we found from there previously 

        """