class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        count = 1

        while num >= count*count:
            if num == count*count:
                return True
            count += 1
        return False
        