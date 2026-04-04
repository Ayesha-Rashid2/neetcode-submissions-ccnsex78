class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n):
            if nums[i] > 0: #if its positve then ur cooked
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, n-1

            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
        return answer
        
        
        




        
        ''' Working o(n^2) solution
        nums.sort()
        k = len(nums)-1
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == [nums[i] - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while right > left:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum  < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1

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