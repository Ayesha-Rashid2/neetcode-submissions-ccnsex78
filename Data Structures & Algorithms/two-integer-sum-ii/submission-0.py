class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        myMap = {}

        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in myMap:
                return [myMap[comp]+1, i+1]
            else:
                myMap[numbers[i]] = i
        