class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1
        bondary_index = 0

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] <= nums[-1]:
                bondary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[bondary_index]


        