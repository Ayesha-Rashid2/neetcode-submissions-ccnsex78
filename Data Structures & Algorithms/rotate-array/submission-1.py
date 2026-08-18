class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        nums.reverse()

        left = 0
        right = k - 1
        while right >= left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = k
        right = len(nums)-1
        while right >= left:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1







    # 7   6   5   4   3   2   1
    # i   i   i   i



            
        