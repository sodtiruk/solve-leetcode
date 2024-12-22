from typing import List

class Solution:
    def __init__(self):
        self.cache = {}

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.findMinimumPath2(triangle, 0, 0)
         
    #first solution 
    def findMinimumPath(self, triangle, row, col) -> int:
        if row >= len(triangle):       
            return 0

        current = triangle[row][col]
        fromLeft = self.findMinimumPath(triangle, row+1, col) 
        fromRight = self.findMinimumPath(triangle, row+1, col+1) 

        return current + min(fromLeft, fromRight) 
    
    #second solution top down 
    def findMinimumPath2(self, triangle, row, col) -> int:
        if row >= len(triangle):       
            return 0

        current = triangle[row][col]

        if (row+1, col) not in self.cache:
            self.cache[(row+1, col)] = self.findMinimumPath2(triangle, row+1, col)       
        if (row+1, col+1) not in self.cache:
            self.cache[(row+1, col+1)] = self.findMinimumPath2(triangle, row+1, col+1)       
        
        return current + min(self.cache[(row+1, col)], self.cache[(row+1, col+1)]) 

solution = Solution()
print(solution.minimumTotal([[-10]]))





