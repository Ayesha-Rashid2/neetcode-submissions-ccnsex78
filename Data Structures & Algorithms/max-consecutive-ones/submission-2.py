class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_num = 0
        
        for right in range(len(nums)):
            if nums[right] == 1:
                max_num = max(max_num, right - left + 1)
            else:
                left = right + 1
        return max_num
                
        