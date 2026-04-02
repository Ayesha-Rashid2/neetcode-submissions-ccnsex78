class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        seen = set()

        row, col = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh_oranges += 1

                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]

        while q and fresh_oranges > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                #if if its in bounds and its fresh, make rotten
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue 
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh_oranges -= 1
            time += 1

        return time if fresh_oranges == 0 else -1




                    
        
        