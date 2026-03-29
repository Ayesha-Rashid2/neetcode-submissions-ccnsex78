class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        while right >= left:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif target > total:
                left += 1
            else:
                right -= 1

        ''' This is the o(n) solution, but we want o(1)
        myMap = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in myMap:
                return [myMap[comp]+1, i+1]
            else:
                myMap[numbers[i]] = i
            '''
        