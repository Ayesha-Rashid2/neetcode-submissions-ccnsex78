class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set()
        nums2_set = set()
        res = []

        for nums in nums1:
            if nums not in nums1_set:
                nums1_set.add(nums)

        for nums in nums2:
            if nums not in nums2_set:
                nums2_set.add(nums)

        
        for nums in nums2_set:
            if nums in nums1_set:
                res.append(nums)
        
        return res
        
        