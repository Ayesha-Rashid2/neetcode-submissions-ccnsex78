class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

            
        heapq.heapify(nums)

        value = 0

        for i in range(k):
            value = -heapq.heappop(nums)

        return value

        