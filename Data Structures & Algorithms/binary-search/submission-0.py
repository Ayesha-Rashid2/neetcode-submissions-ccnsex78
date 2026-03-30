class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while right >= left:
            midp = (right + left) // 2
            val = nums[midp]

            if val < target:
                left = midp + 1
            elif val > target:
                right = midp - 1
            else:
                return midp
        return -1

        