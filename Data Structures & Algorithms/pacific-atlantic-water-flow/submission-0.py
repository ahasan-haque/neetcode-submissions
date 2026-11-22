class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, columns = len(heights), len(heights[0])

        # pacific bfs
        visited_p = set()

        p_q = collections.deque()

        for r in range(rows):
            p_q.append((r, 0))
            visited_p.add((r, 0))

        for c in range(columns):
            p_q.append((0, c))
            visited_p.add((0, c))


        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for d_r, d_c in directions:
                    row = r + d_r
                    col = c + d_c
                    if (
                        row in range(rows) and
                        col in range(columns) and
                        (row, col) not in visited and
                        heights[row][col] >= heights[r][c]):
                            visited.add((row, col))
                            q.append((row, col))
            return visited



        visited_p = bfs(p_q, visited_p)

        # atlantic bfs
        visited_a = set()

        a_q = collections.deque()

        for r in range(rows):
            a_q.append((r, columns - 1))
            visited_a.add((r, columns - 1))

        for c in range(columns):
            a_q.append((rows - 1, c))
            visited_a.add((rows - 1, c))

        visited_a = bfs(a_q, visited_a)

        return list(visited_a & visited_p)



        