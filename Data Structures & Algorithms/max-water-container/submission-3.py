class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left, right = 0, len(heights)-1
       max_area = 0

       while right >= left:
            height = min(heights[left], heights[right])
            width = right - left
            area = height*width
            max_area = max(max_area, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1


       return max_area
            

           







       '''
        max_area = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                area = height*width
                max_area = max(max_area, area)

        return max_area
        '''

