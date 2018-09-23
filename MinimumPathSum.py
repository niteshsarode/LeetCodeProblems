class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(0,len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[i][j]