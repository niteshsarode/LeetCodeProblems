class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid = self.check(i,j,grid)
        return count
    
    def check(self,i,j,grid):
        grid[i][j] = 0
        l = len(grid)
        if (i+1) < l and grid[i+1][j] == "1":
            grid = self.check(i+1,j,grid)
        if (i-1) >= 0 and grid[i-1][j] == "1":
            grid = self.check(i-1,j,grid)
        if (j+1) < len(grid[0]) and grid[i][j+1] == "1":
            grid = self.check(i,j+1,grid)
        if (j-1) >= 0 and grid[i][j-1] == "1":
            grid = self.check(i,j-1,grid)
        return grid