class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        mySet = set(nums)

        for num in nums:
            if num-1 not in mySet:
                next_num = num + 1
                length = 1
                while next_num in mySet:
                    length += 1
                    next_num += 1
                counter = max(counter, length)
        return counter
