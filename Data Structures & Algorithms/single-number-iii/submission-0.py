class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        for k in count:
            if count[k] == 1:
                res.append(k)
        
        return res

            
        