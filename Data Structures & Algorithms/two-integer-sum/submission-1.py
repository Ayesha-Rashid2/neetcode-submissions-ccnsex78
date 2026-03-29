class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        myMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in myMap:
                return [myMap[comp], i]
            else:
                myMap[nums[i]] = i