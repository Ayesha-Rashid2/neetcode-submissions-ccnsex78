class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        cur_color = image[sr][sc]

        if cur_color == color:
            return image

        cur = [[sr, sc]]
        image[sr][sc] = color

        while cur:
            new_layer = []
            for r, c in cur:
                directions = [[r-1, c], [r+1, c], [r, c+1], [r, c-1]]
                for check_r, check_c in directions:
                    if check_r >= 0 and check_c >= 0 and check_r < m and check_c < n and image[check_r][check_c] == cur_color:
                        image[check_r][check_c] = color
                        new_layer.append([check_r, check_c])
            cur = new_layer

        return image
        

        '''
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
        '''



    