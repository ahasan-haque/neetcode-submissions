import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if (row + dr in range(rows) and 
                        col + dc in range(columns) and 
                        grid[row + dr][col + dc] == '1' and 
                        (row + dr, col + dc) not in visited):
                        visited.add((row + dr, col + dc)) 
                        q.append((row + dr, col + dc))


        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1' and (row, column) not in visited:
                    bfs(row, column)
                    islands += 1
                    visited.add((row, column))

        return islands

