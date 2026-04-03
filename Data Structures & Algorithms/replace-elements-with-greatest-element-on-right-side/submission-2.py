class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Initial max of -1
        #Reverse Iteration
        #New max = max(old max, arr[i])

        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr






        ''' 
        Brute Force Solution
        ans = [0] * len(arr)
        for i in range(len(arr)):
            rightMax = -1
            for j in range(i+1,len(arr)):
                rightMax = max(rightMax, arr[j])
            ans[i] = rightMax
        return ans
        '''





        