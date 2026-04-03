class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def dfs(r, c):
            if (r,c) in visited:
                return
            visited.add((r, c))
            directions = [(1,0), (0, 1), (-1, 0), (0,-1)]

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
                    dfs(nr, nc) 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    result += 1
        return result





        '''
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0


        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands
        '''


          
        