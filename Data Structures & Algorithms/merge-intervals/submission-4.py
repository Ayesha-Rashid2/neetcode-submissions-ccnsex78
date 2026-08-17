class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []

        result = []

        intervals.sort()

        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]: #theres no overlap
                result.append(interval)
            else: #there is overlap
                result[-1][1] = max(result[-1][1], interval[1])

        return result




        