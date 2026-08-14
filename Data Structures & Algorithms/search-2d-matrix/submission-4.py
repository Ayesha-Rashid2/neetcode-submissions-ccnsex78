class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        column_count = len(matrix[0])

        total_number_in_matrix = row_count * column_count
        left = 0
        right = total_number_in_matrix - 1
        
        while left <= right:
            middle = (left + right) // 2
            row_index = middle // column_count
            column_index = middle % column_count

            mid_num = matrix[row_index][column_index]
            if target == mid_num:
                return True
            elif target < mid_num:
                right = middle - 1
            else:
                left = middle + 1
            
        return False



        '''
        #Brute Force o(N x M) solution  m is rows n is cols
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False
        '''
        
      
        '''
       m = len(matrix)
       n = len(matrix[0])

       t = m * n
       left = 0
       right = t - 1

       while right >= left:
            m = (left + right) // 2
            i = m // n
            j = m % n

            middle_num = matrix[i][j]

            if target == middle_num:
                return True
            elif target < middle_num:
                right = m - 1
            else:
                left = m + 1
    
       return False
       '''