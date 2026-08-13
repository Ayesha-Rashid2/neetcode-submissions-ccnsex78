class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency_map = {}

        max_num = -1
        for i,num in enumerate(arr):
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1

        for num in frequency_map:
            if num == frequency_map[num]:
                    max_num = max(max_num, num)

        return max_num

        

        