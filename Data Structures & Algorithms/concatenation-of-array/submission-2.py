class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        nums_2 = []
        j = 0

        for i in range(len(nums)):
            nums_2.append(nums[i])

        for i in range(len(nums)):
            nums_2.append(nums[i])
        
        return nums_2            

        