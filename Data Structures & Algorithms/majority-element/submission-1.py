class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = {}

        for num in nums:
            if num in my_map:
                my_map[num] +=  1
            else:
                my_map[num] = 1
        
        return max(my_map, key=my_map.get)
        