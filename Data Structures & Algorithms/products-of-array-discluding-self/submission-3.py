class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = []
        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    product *= nums[j]
            return_list.append(product)
            product = 1
        return return_list