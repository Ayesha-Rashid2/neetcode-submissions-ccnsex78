class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for p in points:
            x = p[0]
            y = p[1]
            distance = math.sqrt((x**2)+(y**2))
            p.insert(0, distance)

        heapq.heapify(points)
        value = []

        for i in range(k):
            closest = heapq.heappop(points)
            value.append(closest[1:])

        return value


        