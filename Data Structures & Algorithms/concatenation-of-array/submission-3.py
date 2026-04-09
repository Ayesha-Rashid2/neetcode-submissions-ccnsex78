class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #nums_2 = []
        '''
        for i in range(len(nums)):
            nums_2.append(nums[i])

        for i in range(len(nums)):
            nums_2.append(nums[i])
        
        
        for i in range(2):
            for n in nums:
                nums_2.append(n)

        '''
        nums2 = []
        for i in range(2):
            for num in nums:
             nums2.append(num)

        return nums2





        