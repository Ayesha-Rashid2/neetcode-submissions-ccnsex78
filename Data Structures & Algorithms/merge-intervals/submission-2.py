class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result_list = []

        for num in intervals:
            if not result_list or result_list[-1][1] < num[0]:
                result_list.append(num)
            else:
                result_list[-1] = [result_list[-1][0], max (result_list[-1][1], num[1])]
        return result_list




        