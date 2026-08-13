class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []

        for a in range(len(nums)-2):
            i = a + 1
            j = len(nums)-1
            if nums[a] > 0:
                break

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            while i < j:
                total = nums[a] + nums[i] + nums[j]
                if total > 0:
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    res.append([nums[i], nums[j], nums[a]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                

        return res






        
        
        
        
        
        
        






        
        
        
        
        
        
        '''
        nums.sort()
        k = len(nums)-1
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while right > left:
                total = a + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([a,nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res
        
            
'''

        
        ''' Brute Force Solution
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(t) for t in res]
        '''