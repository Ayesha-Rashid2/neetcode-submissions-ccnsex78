class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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