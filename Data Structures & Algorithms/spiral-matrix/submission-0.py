class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            #add first row of matrix
            res += (matrix.pop(0)) #pop from index 0, the front

            # append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())


            #add reverse of the last element
            if matrix and matrix[-1]:
                res += matrix.pop()[::-1]

            #append the fist element of each row in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res



            
            

        