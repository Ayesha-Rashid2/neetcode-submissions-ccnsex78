class Solution:
    def isPathCrossing(self, path: str) -> bool:
        location = set()
        x, y = 0, 0
        location.add((x,y))
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1

            if (x,y) in location:
                return True
            location.add((x,y))
        return False