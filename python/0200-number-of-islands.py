# bfs approach
class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i, j):
            queue = [[i, j]]
            visited.add((i, j))
            while queue:
                row, col = queue.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    new_row, new_col = dr + row, dc + col
                    if new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == '1' and (new_row, new_col) not in visited:
                        queue.append([new_row, new_col])
                        visited.add((new_row, new_col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands
