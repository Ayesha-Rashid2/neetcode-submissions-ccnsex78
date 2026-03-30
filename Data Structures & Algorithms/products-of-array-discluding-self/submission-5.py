class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        return_list = []
        product = 1
        #Brute Force:
        for i in range (len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            return_list.append(product)
            product = 1
        return return_list

    