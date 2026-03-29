class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        return_list = []
        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1

        for i in range(k):
            max_key = max(myMap, key=myMap.get)
            return_list.append(max_key)
            del myMap[max_key]

        return return_list