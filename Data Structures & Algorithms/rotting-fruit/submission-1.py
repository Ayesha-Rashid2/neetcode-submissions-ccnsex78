class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = []
        rows, cols = len(grid), len(grid[0])
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten.append((row, col))


        while rotten and fresh > 0:
            minutes += 1
            curr = []

            for r, c in rotten:
                check = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
                for i, j in check:
                    if i >= 0 and j >= 0 and i < rows and j < cols and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        curr.append((i,j))

                        if fresh == 0:
                            return minutes
            rotten = curr
        if fresh == 0:
            return minutes
        else:
            return -1



        
        
        
        
        
        
        
        
        
        
        
        
        '''
        time = 0

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
        '''




                    
        
        