class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()

        for i, num in enumerate(nums):
            if num in mySet:
                return num
            mySet.add(num)

        return num

        