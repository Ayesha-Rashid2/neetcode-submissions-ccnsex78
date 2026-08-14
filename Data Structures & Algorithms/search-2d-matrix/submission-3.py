class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            num = matrix[i]
            left = 0
            right = len(num) - 1
            while left <= right:
                mid = (left+right)//2
                if target == num[mid]:
                    return True
                elif target < num[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            continue
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