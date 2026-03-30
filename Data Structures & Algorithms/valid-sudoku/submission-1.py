class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Rows
        for i in range(len(board)):
            mySetRow = set()
            for j in range(len(board[i])):
                item = board[i][j]
                if item in mySetRow:
                    return False
                elif item != '.':
                    mySetRow.add(item)

        #Columns
        for i in range(len(board)):
            mySetCol = set()
            for j in range(len(board[i])):
                item = board[j][i]
                if item in mySetCol:
                    return False
                elif item != '.':
                    mySetCol.add(item)

        #Threes
        starts = [(0,0), (0,3), (0,6), (3, 0), (3,3), (3, 6), 
        (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            mySetThree = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in mySetThree:
                        return False
                    elif item != '.':
                        mySetThree.add(item)
            
        return True

               
        