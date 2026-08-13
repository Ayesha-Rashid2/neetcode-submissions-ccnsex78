class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        my_map = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in my_map:
                return [my_map[comp], i]
            
            my_map[num] = i


















        '''
        myMap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in myMap:
                return [myMap[comp], i]
            else:
                myMap[num] = i

        '''

        ''' Brute Force Solution
        for i in range(len(nums)):
            comp = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == comp:
                    return [i, j]

            '''