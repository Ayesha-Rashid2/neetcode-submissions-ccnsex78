class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            return_list[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            return_list[i] *= postfix
            postfix *= nums[i]
        return return_list

        
         
        
        
        """return_list = []
        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    product *= nums[j]
            return_list.append(product)
            product = 1
        return return_list """