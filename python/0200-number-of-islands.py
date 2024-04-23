class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(i, j):
            queue = [[i, j]]
            visited.add((i, j))
            while queue:
                nrow, ncol = queue.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row, col = nrow + dr, ncol + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == '1' and (row, col) not in visited:
                        queue.append([row, col])
                        visited.add((row, col))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
