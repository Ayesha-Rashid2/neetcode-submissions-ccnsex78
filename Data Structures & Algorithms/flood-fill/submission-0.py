class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image

        def fill(sr, sc):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != original:
                return

            image[sr][sc] = color

            fill(sr - 1, sc)
            fill(sr + 1, sc)
            fill(sr, sc - 1)
            fill(sr, sc + 1)

        fill(sr, sc)
        return image